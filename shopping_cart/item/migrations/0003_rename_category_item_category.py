# Generated by Django 4.2.5 on 2023-10-01 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Category',
            new_name='category',
        ),
    ]
