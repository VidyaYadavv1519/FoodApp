# Generated by Django 2.2 on 2023-06-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://png.pngtree.com/png-vector/20191019/ourmid/pngtree-plate-and-cutlery-icon-black-monochrome-style-png-image_1831171.jpg', max_length=500),
        ),
    ]
