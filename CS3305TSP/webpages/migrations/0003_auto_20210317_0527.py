# Generated by Django 3.1.5 on 2021-03-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_auto_20210317_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.CharField(blank=True, editable=False, max_length=766),
        ),
    ]
