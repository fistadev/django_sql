from django.contrib import admin
from .models import *

class BuildingDataAdmin(admin.ModelAdmin):
    model = BuildingData
    list_display = ('id', 'name')
    list_filter = ('name', )


class MeterDataAdmin(admin.ModelAdmin):
    model = MeterData


class HalfHourlyDataAdmin(admin.ModelAdmin):
    model = HalfHourlyData

admin.site.register(BuildingData, BuildingDataAdmin)
admin.site.register(MeterData, MeterDataAdmin)
admin.site.register(HalfHourlyData, HalfHourlyDataAdmin)
# admin.site.register(BuildingDataAdmin, MeterDataAdmin, HalfHourlyDataAdmin)