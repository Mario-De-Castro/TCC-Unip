from django.contrib import admin
from api.models import Fires, Weather

# Register your models here.
class FiresAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'city', 'state', 'biome', 'weather')
    list_display_links = ('id', 'weather')
    search_fields = ('id',)
    list_per_page = 20

class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'temp', 'feels_like', 'humidity', 'pressure', 'dew_point', 'wind_speed', 'wind_gust', 'wind_deg')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20

admin.site.register(Fires, FiresAdmin)
admin.site.register(Weather, WeatherAdmin)
