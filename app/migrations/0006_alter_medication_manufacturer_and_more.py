# Generated by Django 4.2 on 2023-05-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_dispense_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='Manufacturer',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='medication',
            name='Med_Name',
            field=models.CharField(max_length=20),
        ),
    ]
