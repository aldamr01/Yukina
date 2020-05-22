# Django
from django.shortcuts import get_object_or_404

# Library
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Application
from app.dashboard.app_models.dashboard import SensorCurrentValue, SensorControl

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

class GetDataControl(APIView):
    permission_classes = (IsAuthenticated,)
   
    def get(self, request):
            sensor_control = SensorControl.objects.get(user_id=request.user.id)
            return Response(
                {
                    'status_code': 200,
                    'status': sensor_control.status,
                    'pump_nutrient_a': sensor_control.pump_nutrient_a,
                    'pump_nutrient_b': sensor_control.pump_nutrient_b,
                    'pump_water': sensor_control.pump_water,                    
                }, 
                status = status.HTTP_200_OK
            )
  
            
class SetDataControlStage1(APIView):
   
    def get(self):
            sensor_control = SensorControl.objects.get(user_id=1)
            sensor_control.status = True
            sensor_control.pump_nutrient_a = True
            sensor_control.pump_nutrient_b = False
            sensor_control.pump_water = False
            return Response(
                {
                    'status_code': 200,                                       
                }, 
                status = status.HTTP_200_OK
            )
            

class SetDataControlStage2(APIView):
   
    def get(self):
            sensor_control = SensorControl.objects.get(user_id=1)
            sensor_control.status = True
            sensor_control.pump_nutrient_a = False
            sensor_control.pump_nutrient_b = True
            sensor_control.pump_water = False
            return Response(
                {
                    'status_code': 200,                                       
                }, 
                status = status.HTTP_200_OK
            )


class SetDataControlStage3(APIView):
   
    def get(self):
            sensor_control = SensorControl.objects.get(user_id=1)
            sensor_control.status = True
            sensor_control.pump_nutrient_a = False
            sensor_control.pump_nutrient_b = False
            sensor_control.pump_water = True
            return Response(
                {
                    'status_code': 200,                                       
                }, 
                status = status.HTTP_200_OK
            )


class SetDataControlStage4(APIView):
       
    def get(self):
            sensor_control = SensorControl.objects.get(user_id=1)
            sensor_control.status = False
            sensor_control.pump_nutrient_a = False
            sensor_control.pump_nutrient_b = False
            sensor_control.pump_water = False
            return Response(
                {
                    'status_code': 200,                                       
                }, 
                status = status.HTTP_200_OK
            )