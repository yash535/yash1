# Generated by Django 3.0.3 on 2020-04-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='test_score',
            field=models.IntegerField(default=0, help_text='Your Test Score'),
        ),
    ]
