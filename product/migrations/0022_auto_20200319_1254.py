# Generated by Django 3.0.1 on 2020-03-19 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='custid',
            field=models.CharField(default='0000', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderid',
            field=models.CharField(default='0000', max_length=20),
        ),
    ]
