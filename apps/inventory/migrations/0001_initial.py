# Generated by Django 4.1.1 on 2022-10-09 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base_model', '0005_branch_created_at_branch_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('inventory_date', models.DateField(verbose_name='Inventory date')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('gln_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_model.branch', verbose_name='Branch')),
                ('gln_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_model.product', verbose_name='Product')),
                ('gln_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]