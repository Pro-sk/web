# Generated by Django 3.0.1 on 2020-03-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20200318_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uphone', models.CharField(default='', max_length=50)),
                ('pname', models.CharField(default='', max_length=50)),
                ('pdesc', models.CharField(max_length=200)),
                ('pcategory', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('pimg', models.ImageField(upload_to='')),
                ('orderid', models.IntegerField()),
                ('custid', models.IntegerField()),
                ('jsondata', models.CharField(max_length=1000)),
            ],
        ),
    ]
