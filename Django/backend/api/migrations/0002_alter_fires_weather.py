# Generated by Django 4.0.6 on 2022-08-12 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fires',
            name='weather',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.weather', verbose_name='Condições Climaticas'),
        ),
    ]
