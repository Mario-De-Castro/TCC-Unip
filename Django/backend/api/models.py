from pyexpat import model
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
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE, verbose_name='Condições Climaticas')
