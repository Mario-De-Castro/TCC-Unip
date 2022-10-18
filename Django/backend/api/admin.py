from django.contrib import admin
from api.models import DataFire

class DataFiresAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'type')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20

admin.site.register(DataFire, DataFiresAdmin)
