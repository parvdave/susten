# Generated by Django 4.2.10 on 2024-02-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sustenuser', '0002_rename_user_name_treehacksuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='treehacksuser',
            name='levels',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='treehacksuser',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
