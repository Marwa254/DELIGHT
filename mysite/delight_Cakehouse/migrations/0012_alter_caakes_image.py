# Generated by Django 4.1.4 on 2023-02-26 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delight_Cakehouse", "0011_caakes_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="caakes",
            name="Image",
            field=models.ImageField(
                default="default.jpg",
                upload_to="home/marwa254/Desktop/DELIGHT/mysite/delight_Cakehouse/static/images",
            ),
        ),
    ]
