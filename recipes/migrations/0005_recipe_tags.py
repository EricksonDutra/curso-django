# Generated by Django 4.0.1 on 2022-06-01 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_remove_tag_content_type_remove_tag_object_id'),
        ('recipes', '0004_merge_0002_auto_20211130_0929_0003_alter_recipe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag'),
        ),
    ]
