# Generated by Django 4.1.2 on 2022-10-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_remove_inventory_branch_remove_inventory_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='unit_value',
            field=models.FloatField(null=True, verbose_name='Unit value'),
        ),
    ]
