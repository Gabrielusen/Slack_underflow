# Generated by Django 3.0.6 on 2020-07-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20200708_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postanswer',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='published'),
        ),
    ]