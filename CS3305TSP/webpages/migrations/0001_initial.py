# Generated by Django 3.1.5 on 2021-03-21 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import webpages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_description', models.TextField(blank=True, null=True)),
                ('address_line_1', models.CharField(max_length=255, verbose_name='Street address')),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='District or Townland')),
                ('city', models.CharField(default='', max_length=128, verbose_name='City or town')),
                ('county', models.CharField(choices=[('Antrim', 'Antrim'), ('Armagh', 'Armagh'), ('Carlow', 'Carlow'), ('Cavan', 'Cavan'), ('Clare', 'Clare'), ('Cork', 'Cork'), ('Donegal', 'Donegal'), ('Down', 'Down'), ('Dublin', 'Dublin'), ('Fermanagh', 'Fermanagh'), ('Galway', 'Galway'), ('Kerry', 'Kerry'), ('Kildare', 'Kildare'), ('Kilkenny', 'Kilkenny'), ('Laois', 'Laois'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Londonderry', 'Londonderry'), ('Longford', 'Longford'), ('Louth', 'Louth'), ('Mayo', 'Mayo'), ('Meath', 'Meath'), ('Monaghan', 'Monaghan'), ('Offaly', 'Offaly'), ('Roscommon', 'Roscommon'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Tyrone', 'Tyrone'), ('Waterford', 'Waterford'), ('Westmeath', 'Westmeath'), ('Wexford', 'Wexford'), ('Wicklow', 'Wicklow')], default='', max_length=128)),
                ('floor_plan', models.ImageField(blank=True, null=True, upload_to='floor_plan')),
                ('property_type', models.CharField(choices=[('Detached House', 'Detached House'), ('Semi-detached House', 'Semi-detached House'), ('Terraced House', 'Terraced House'), ('Duplex', 'Duplex')], default='', max_length=128)),
                ('number_of_bedrooms', models.PositiveIntegerField()),
                ('number_of_bathrooms', models.PositiveIntegerField()),
                ('energy_rating', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('D1', 'D1'), ('D2', 'D2'), ('E1', 'E1'), ('E2', 'E2'), ('F', 'F'), ('G', 'G')], default='', max_length=128)),
                ('size', models.PositiveIntegerField(verbose_name='Size (m<sup>2</sup>)')),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Price (&euro;)')),
                ('estimated_price', models.PositiveIntegerField(blank=True, editable=False)),
                ('address', models.CharField(blank=True, editable=False, max_length=766)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=webpages.models.get_image_filename, verbose_name='images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_images', to='webpages.post')),
            ],
        ),
    ]
