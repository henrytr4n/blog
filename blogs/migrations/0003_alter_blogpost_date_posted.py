# Generated by Django 4.1 on 2022-09-03 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_remove_blogpost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
