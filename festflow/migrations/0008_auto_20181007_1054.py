# Generated by Django 2.0.2 on 2018-10-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0007_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(null=True, upload_to='gallery_images/'),
        ),
    ]
