# Generated by Django 3.0.6 on 2020-07-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postanswer',
            name='active',
        ),
        migrations.AddField(
            model_name='postanswer',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]