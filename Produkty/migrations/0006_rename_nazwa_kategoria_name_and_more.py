# Generated by Django 4.2 on 2023-04-04 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0005_kategoria_produkty_kategoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kategoria',
            old_name='nazwa',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='produkty',
            old_name='tytuł',
            new_name='nazwa',
        ),
    ]
