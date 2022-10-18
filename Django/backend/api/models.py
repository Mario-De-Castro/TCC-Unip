from django.db import models

class DataFire(models.Model):
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')
    bright_ti4 = models.FloatField(verbose_name='Bright')
    scan = models.FloatField(verbose_name='Scan')
    track = models.FloatField(verbose_name='Bright')
    acq_date = models.DateField(verbose_name="Data da Queimada")
    acq_time = models.CharField(verbose_name="Hora que foi tirado", max_length=255)
    satellite = models.CharField(verbose_name="Satelite", max_length=255)
    instrument = models.CharField(verbose_name="Tipo do Dataset", max_length=255)
    confidence = models.CharField(verbose_name="Confiabilidade", max_length=255)
    version = models.IntegerField(verbose_name="Versão")
    bright_ti5 = models.FloatField(verbose_name='Bright')
    frp = models.FloatField(verbose_name='FRP')
    daynight = models.CharField(verbose_name="Dia ou Noite", max_length=255)
    type = models.IntegerField(verbose_name="Tipo do Local")