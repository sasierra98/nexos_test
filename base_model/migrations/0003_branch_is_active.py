# Generated by Django 4.1.1 on 2022-10-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_model', '0002_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
