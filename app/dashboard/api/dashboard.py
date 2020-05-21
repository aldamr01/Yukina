# Django
from django.shortcuts import get_object_or_404

# Library
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Application
from app.dashboard.app_models.dashboard import SensorCurrentValue

class CurrentSensorValue(APIView):
   permission_classes = (IsAuthenticated,)
   
   def get(self, request):
        sensor_value = SensorCurrentValue.objects.get(user_id=request.user.id)
        return Response(
            {
                'status_code': 200,
                'value_tds': sensor_value.value_tds,
                'value_ph': sensor_value.value_ph,
                'value_humidity': sensor_value.value_humidity,
                'value_water_temperature': sensor_value.value_water_temperature,
                'value_air_temperature': sensor_value.value_air_temperature,
            }, 
            status = status.HTTP_200_OK
        )