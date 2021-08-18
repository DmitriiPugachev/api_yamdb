from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db.models.aggregates import Avg
from rest_framework import serializers, validators
from rest_framework.relations import SlugRelatedField

from reviews.models import Category, Comment, Genre, Review, Title

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Review
        read_only_fields = ('author', 'title')

    def create(self, validated_data):
        title = validated_data.pop('title_id')
        if Review.objects.filter(
            author=self.context['request'].user,
            title_id=title
        ).exists():
            raise serializers.ValidationError(
                "You can send only one review for one title.")

        return Review.objects.create(title_id=title, ** validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'review')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        model = User


class UserMeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        model = User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email')
        model = User

    def validate(self, data):
        if data['username'] == 'me':
            raise validators.ValidationError(
                'You can not use this username.'
            )
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    category = SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
        required=False
    )
    genre = SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
        required=False
    )

    def validate(self, year):
        if year > datetime.now().year or year < 1000:
            raise ValidationError(
                ('Укажите 4-х значиный год, не больше текущего года'),
                params={'year': year},
        )


    def get_rating(self, obj):
        rating = Review.objects.filter(title=obj.id).aggregate(Avg('score'))
        if rating['score__avg'] is None:
            return None
        return rating['score__avg']

    class Meta:
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')
        model = Title
