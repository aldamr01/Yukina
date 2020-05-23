# Django
from django.contrib import admin

# Application
from app.dashboard.app_models import dashboard


# Register your models here.
admin.site.register(dashboard.SensorCurrentValue)
admin.site.register(dashboard.SensorValue)
admin.site.register(dashboard.SensorControl)
admin.site.register(dashboard.SensorConfig)
admin.site.register(dashboard.NutrientValue)