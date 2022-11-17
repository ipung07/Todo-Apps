# Generated by Django 4.1.3 on 2022-11-17 07:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_todo_todo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='img/todo/', validators=[django.core.validators.validate_image_file_extension]),
        ),
    ]