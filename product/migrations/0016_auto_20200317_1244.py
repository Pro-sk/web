# Generated by Django 3.0.1 on 2020-03-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20200317_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='uname',
            field=models.CharField(default='', max_length=50, verbose_name='Username'),
        ),
    ]
