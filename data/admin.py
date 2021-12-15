from django.contrib import admin
from .models import *

class BuildingDataAdmin(admin.ModelAdmin):
    model = BuildingData


# class MeterDataAdmin(admin.ModelAdmin):
#     model = MeterData


# class HalfHourlyDataAdmin(admin.ModelAdmin):
#     model = HalfHourlyData

admin.site.register(BuildingData, BuildingDataAdmin)
# admin.site.register(BuildingDataAdmin, MeterDataAdmin, HalfHourlyDataAdmin)