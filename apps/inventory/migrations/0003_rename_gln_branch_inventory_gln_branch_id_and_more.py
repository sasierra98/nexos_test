# Generated by Django 4.1.1 on 2022-10-09 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_inventory_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='gln_branch',
            new_name='gln_branch_id',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='gln_product',
            new_name='gln_product_id',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='gln_user',
            new_name='gln_user_id',
        ),
    ]