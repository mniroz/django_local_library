# Generated by Django 4.1 on 2022-08-11 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('catalog.can_mark_returned', 'Set book as returned'),)},
        ),
    ]
