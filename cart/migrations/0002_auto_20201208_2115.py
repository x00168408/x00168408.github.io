# Generated by Django 3.1.4 on 2020-12-08 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartProd',
            new_name='CartItem',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='CartItem',
        ),
    ]