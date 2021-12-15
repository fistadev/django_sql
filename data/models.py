from django.db import models

# Create your models here.

class BuildingData(models.Model):
    id = models.IntegerField()
    name = models.CharField()

    def __str__(self):
        return self.id


class MeterData(models.Model):
    building_id = models.ForeignKey(BuildingData, on_delete=models.CASCADE)
    id = models.IntegerField()
    fuel = models.CharField()
    unit = models.CharField()

    def __str__(self):
        return self.id


class HalfHourlyData(models.Model):
    consumption = models.FloatField()
    meter_id = models.ForeignKey(MeterData, on_delete=models.CASCADE)
    reading_date_time = models.DateTimeField()
