# Generated by Django 4.2.17 on 2024-12-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDekho_app', '0002_carlist_chassisnumber_carlist_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showroomlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
    ]
