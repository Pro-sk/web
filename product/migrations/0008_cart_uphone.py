# Generated by Django 3.0.1 on 2020-01-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='uphone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
