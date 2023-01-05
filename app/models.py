from django.db import models

class Maps(models.Model):
    alamat = models.CharField(max_length=200, null=True, blank=True)
    lokasi = models.CharField(max_length=200, null=True, blank=True)

class Crud(models.Model):
    nama = models.CharField(max_length=200, null=True, blank=True)
    keterangan = models.CharField(max_length=200, null=True, blank=True)
    lokasi = models.CharField(max_length=200, null=True, blank=True)
