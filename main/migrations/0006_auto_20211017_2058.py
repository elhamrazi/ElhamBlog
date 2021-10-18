# Generated by Django 3.2.8 on 2021-10-17 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_approved_comment_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='Post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.post'),
            preserve_default=False,
        ),
    ]
