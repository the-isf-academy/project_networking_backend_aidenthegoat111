# Generated by Django 5.1.2 on 2024-10-23 07:49

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_categories_prompt'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='categories',
            field=banjo.models.StringField(default=''),
        ),
    ]