# Generated by Django 4.0.6 on 2022-08-10 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(verbose_name='Temperatura')),
                ('feels_like', models.FloatField(verbose_name='Sensação Termica')),
                ('humidity', models.FloatField(verbose_name='Umidade')),
                ('pressure', models.IntegerField(verbose_name='Pressão Atmosferica')),
                ('dew_point', models.FloatField(verbose_name='Formação de Orvalho')),
                ('wind_speed', models.FloatField(verbose_name='Velocidade do vento')),
                ('wind_gust', models.FloatField(verbose_name='Rajada de vento')),
                ('wind_deg', models.IntegerField(verbose_name='Direção do vento')),
            ],
        ),
        migrations.CreateModel(
            name='Fires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('city', models.CharField(max_length=255, verbose_name='Cidade')),
                ('state', models.CharField(max_length=255, verbose_name='Estado')),
                ('country', models.CharField(max_length=255, verbose_name='Pais')),
                ('biome', models.CharField(choices=[('CITY', 'CIDADE'), ('FOREST', 'FLORESTA')], default='FOREST', max_length=255, verbose_name='Bioma')),
                ('weather', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.weather', verbose_name='Condições Climaticas')),
            ],
        ),
    ]