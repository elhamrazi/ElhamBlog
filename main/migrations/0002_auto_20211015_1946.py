# Generated by Django 3.2.8 on 2021-10-15 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='Post',
        ),
    ]
