from django.db import models

# Create your models here.

class BuildingData(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class MeterData(models.Model):
    building_id = models.ForeignKey(BuildingData, on_delete=models.CASCADE, unique=False)
    id = models.IntegerField(primary_key=True)
    fuel = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class HalfHourlyData(models.Model):
    consumption = models.FloatField()
    meter_id = models.ForeignKey(MeterData, on_delete=models.CASCADE, unique=False)
    reading_date_time = models.DateTimeField()
