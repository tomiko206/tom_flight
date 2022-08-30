# Generated by Django 3.2.8 on 2022-08-29 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_ticket_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='Destination_Countrie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Destination_Countrie', to='base.countrie'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='Origin_Countrie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Origin_Countrie', to='base.countrie'),
        ),
    ]
