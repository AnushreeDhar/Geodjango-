from django.contrib import admin
from .models import Incidences, Counties
# Register your models here.
from leaflet.admin import LeafletGeoAdmin
class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ['name', 'location']

class CountiesAdmin(LeafletGeoAdmin):
    list_display = ['counties', 'codes']

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)