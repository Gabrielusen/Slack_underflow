# Generated by Django 3.0.6 on 2020-06-24 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postanswer',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='postanswer',
            old_name='pub_date',
            new_name='created_on',
        ),
    ]
