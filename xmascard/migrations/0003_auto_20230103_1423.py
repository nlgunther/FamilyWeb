# Generated by Django 2.2.25 on 2023-01-03 22:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xmascard', '0002_lists'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lists',
            new_name='List',
        ),
    ]
