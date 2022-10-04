from django.db import models

# Create your models here.

class Weather(models.Model):

    temp = models.FloatField(verbose_name='Temperatura')
    feels_like = models.FloatField(verbose_name='Sensação Termica')
    humidity = models.FloatField(verbose_name='Umidade')
    pressure = models.IntegerField(verbose_name='Pressão Atmosferica')
    dew_point = models.FloatField(verbose_name='Formação de Orvalho')
    wind_speed = models.FloatField(verbose_name='Velocidade do vento')
    wind_gust = models.FloatField(verbose_name='Rajada de vento')
    wind_deg = models.IntegerField(verbose_name='Direção do vento')

class Fires(models.Model):
    BIOMES = (
        ('CITY', 'CIDADE'),
        ('FOREST', 'FLORESTA'),
    )

    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')
    city = models.CharField(verbose_name='Cidade', max_length=255)
    state = models.CharField(verbose_name='Estado', max_length=255)
    country = models.CharField(verbose_name='Pais', max_length=255)
    biome = models.CharField(verbose_name='Bioma', max_length=255, choices=BIOMES, blank=False, null=False, default='FOREST')
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE, verbose_name='Condições Climaticas', null=True)

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