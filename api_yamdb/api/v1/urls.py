from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, ReviewViewSet, TitleViewSet,
                    create_new_user, create_access_token,
                    GenreViewSet, CategoryViewSet)


router_v1 = DefaultRouter(trailing_slash='optional')
router_v1.register('titles/?', TitleViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<titles_id>\d+)/reviews/?',
    ReviewViewSet, basename="reviews")
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments/?',
    CommentViewSet, basename="comments")
router_v1.register('genres/?', GenreViewSet, basename='genres')
router_v1.register('categories/?', CategoryViewSet, basename='categories')


urlpatterns = [
     
    path('auth/signup/', create_new_user, name='create_new_user'),
    path('auth/token/', create_access_token, name='create_access_token'),
    path('', include(router_v1.urls)),    

]
