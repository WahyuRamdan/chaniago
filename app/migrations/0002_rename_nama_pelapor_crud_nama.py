# Generated by Django 4.1.5 on 2023-01-05 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crud',
            old_name='nama_pelapor',
            new_name='nama',
        ),
    ]
