# Generated by Django 4.2.13 on 2024-05-23 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliance',
            name='power_demands',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
