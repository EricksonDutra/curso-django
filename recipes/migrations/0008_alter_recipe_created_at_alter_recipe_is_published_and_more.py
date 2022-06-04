# Generated by Django 4.0.1 on 2022-06-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_options_alter_recipe_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='is published'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_steps',
            field=models.TextField(verbose_name='preparation steps'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_steps_is_html',
            field=models.BooleanField(default=False, verbose_name='preparation steps is html'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.IntegerField(verbose_name='preparation time'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time_unit',
            field=models.CharField(max_length=65, verbose_name='preparation time unit'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings_unit',
            field=models.CharField(max_length=65, verbose_name='servings unit'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
    ]
