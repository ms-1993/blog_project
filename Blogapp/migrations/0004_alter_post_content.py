# Generated by Django 4.0.1 on 2022-01-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
