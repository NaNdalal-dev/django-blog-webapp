# Generated by Django 3.2.5 on 2021-07-29 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_articles', '0003_alter_blog_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Data',
            new_name='Date',
        ),
    ]
