# Generated by Django 4.0.1 on 2022-06-04 01:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0006_alter_recipe_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=165, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='is_published'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_steps',
            field=models.TextField(verbose_name='preparation_steps'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_steps_is_html',
            field=models.BooleanField(default=False, verbose_name='preparation_steps_is_html'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.IntegerField(verbose_name='preparation_time'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time_unit',
            field=models.CharField(max_length=65, verbose_name='preparation_time_unit'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(verbose_name='servings'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings_unit',
            field=models.CharField(max_length=65, verbose_name='servings_unit'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=65, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_at'),
        ),
    ]
