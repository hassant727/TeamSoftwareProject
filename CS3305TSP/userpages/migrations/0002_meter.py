# Generated by Django 3.1.5 on 2021-02-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('reading', models.IntegerField()),
            ],
            options={
                'ordering': ('-date', 'name'),
            },
        ),
    ]
