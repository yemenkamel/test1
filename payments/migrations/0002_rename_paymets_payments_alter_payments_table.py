# Generated by Django 4.2.14 on 2024-08-02 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Paymets',
            new_name='Payments',
        ),
        migrations.AlterModelTable(
            name='payments',
            table='payments',
        ),
    ]