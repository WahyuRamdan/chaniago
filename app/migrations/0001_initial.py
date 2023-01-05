# Generated by Django 4.1.5 on 2023-01-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelapor', models.CharField(blank=True, max_length=200, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=200, null=True)),
                ('lokasi', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alamat', models.CharField(blank=True, max_length=200, null=True)),
                ('lokasi', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
