# Generated by Django 3.2.5 on 2021-08-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_coupon_cupongroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(blank=True, max_length=8, unique=True),
        ),
    ]
