# Generated by Django 3.1.5 on 2021-02-12 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_remove_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='property_description',
        ),
    ]
