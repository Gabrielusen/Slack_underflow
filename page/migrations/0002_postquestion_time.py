# Generated by Django 3.0.6 on 2020-07-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postquestion',
            name='time',
            field=models.DateField(auto_now=True, verbose_name='date published'),
        ),
    ]
