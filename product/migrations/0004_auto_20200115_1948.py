# Generated by Django 3.0.1 on 2020-01-15 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200115_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='harddisk',
            new_name='HardDisk',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='pimg',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='memory',
            new_name='Memory',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='pcategory',
            new_name='Product Category',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='pdesc',
            new_name='Product Description',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='pname',
            new_name='Product Name',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='battery',
            new_name='Battery',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='camera',
            new_name='Camera',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='pimg',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='memory',
            new_name='Memory',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='pcategory',
            new_name='Product Category',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='pdesc',
            new_name='Product Description',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='pname',
            new_name='Product Name',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='pscategory',
        ),
    ]
