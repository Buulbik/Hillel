# Generated by Django 4.0.6 on 2022-10-06 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_productset'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productset',
            old_name='product',
            new_name='products',
        ),
    ]
