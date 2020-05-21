from django.db import models
from django.contrib.auth.models import User


class SensorCurrentValue(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value_tds = models.FloatField(default=0, null=False)
    value_ph = models.FloatField(default=0, null=False)
    value_humidity = models.FloatField(default=0, null=False)
    value_air_temperature = models.FloatField(default=0, null=False)
    value_water_temperature = models.FloatField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class SensorValue(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value_tds = models.FloatField(default=0, null=False)
    value_ph = models.FloatField(default=0, null=False)
    value_humidity = models.FloatField(default=0, null=False)
    value_air_temperature = models.FloatField(default=0, null=False)
    value_water_temperature = models.FloatField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class SensorConfig(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    min_tds = models.FloatField(default=0, null=False)
    max_tds = models.FloatField(default=0, null=False)
    min_ph = models.FloatField(default=0, null=False)
    max_ph = models.FloatField(default=0, null=False)
    min_humidity = models.FloatField(default=0, null=False)
    max_humidity = models.FloatField(default=0, null=False)
    min_water_temperature = models.FloatField(default=0, null=False)
    max_water_temperature = models.FloatField(default=0, null=False)
    min_air_temperature = models.FloatField(default=0, null=False)
    max_air_temperature = models.FloatField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class NutrientValue(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(null=False, default=500)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)