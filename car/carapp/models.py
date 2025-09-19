from django.db import models
from django.contrib import admin

class Car(models.Model):
    car_brand = models.CharField()
    car_model = models.CharField()
    release_date = models.IntegerField()
    fuel_type = models.CharField()
    car_colour = models.CharField()

    
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'release_date', 'fuel_type', 'car_colour')