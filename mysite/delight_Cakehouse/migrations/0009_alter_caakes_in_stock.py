# Generated by Django 4.1.4 on 2023-02-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delight_Cakehouse", "0008_caakes_in_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="caakes",
            name="in_stock",
            field=models.BooleanField(default=True, verbose_name=False),
        ),
    ]
