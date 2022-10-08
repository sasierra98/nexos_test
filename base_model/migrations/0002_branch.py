# Generated by Django 4.1.1 on 2022-10-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('gln_branch', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='GLN branch')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
    ]
