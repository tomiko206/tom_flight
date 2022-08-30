# Generated by Django 3.2.8 on 2022-07-13 08:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0014_auto_20220712_1517'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Airline_Compamie',
            new_name='Airline_Companie',
        ),
        migrations.RenameField(
            model_name='airline_companie',
            old_name='Country',
            new_name='Countrie',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='Airline_Company',
            new_name='Airline_Companie',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='Destination_Country',
            new_name='Destination_Countrie',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='Origin_Country',
            new_name='Origin_Countrie',
        ),
    ]
