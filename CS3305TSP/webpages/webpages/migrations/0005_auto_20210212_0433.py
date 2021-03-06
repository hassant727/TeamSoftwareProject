# Generated by Django 3.1.5 on 2021-02-12 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_auto_20210212_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address_line_1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='post',
            name='county',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='post_images'),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]