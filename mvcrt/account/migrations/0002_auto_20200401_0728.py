# Generated by Django 3.0.4 on 2020-03-31 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='email',
            new_name='account_name',
        ),
        migrations.AlterModelTable(
            name='account',
            table='accounts',
        ),
    ]
