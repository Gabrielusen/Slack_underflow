# Generated by Django 3.0.6 on 2020-07-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20200712_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postquestion',
            name='text_content',
            field=models.TextField(),
        ),
    ]