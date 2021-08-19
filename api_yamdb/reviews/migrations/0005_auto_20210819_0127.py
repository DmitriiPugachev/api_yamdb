# Generated by Django 2.2.16 on 2021-08-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0004_auto_20210818_2256"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="review",
            name="unique_togather_title_author",
        ),
        migrations.AlterField(
            model_name="title",
            name="description",
            field=models.CharField(
                blank=True,
                max_length=200,
                null=True,
                verbose_name="Описание произведения",
            ),
        ),
        migrations.AddConstraint(
            model_name="review",
            constraint=models.UniqueConstraint(
                fields=("title", "author"),
                name="unique_together_title_author",
            ),
        ),
    ]