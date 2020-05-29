# Django
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
# Library
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import paho.mqtt.client as mqtt

# Application
from app.dashboard.app_models.dashboard import SensorCurrentValue, SensorControl, NutrientValue


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
   
    def get(self, request):
            sensor_control = SensorControl.objects.get(user_id=1)
            nutrient_value = NutrientValue.objects.get(user_id=1)
            nutrient_value.value = nutrient_value.value - 25.0
            nutrient_value.save()
            sensor_control.status = True
            sensor_control.pump_nutrient_a = True
            sensor_control.pump_nutrient_b = False
            sensor_control.pump_water = False
            sensor_control.save()
            return Response(
                {
                    'status_code': 200,                                       
                }, 
                status = status.HTTP_200_OK
            )
            

class SetDataControlStage2(APIView):
   
    def get(self, request):
            sensor_control = SensorControl.objects.get(user_id=1)
            sensor_control.status = True
            sensor_control.pump_nutrient_a = False
            sensor_control.pump_nutrient_b = True
            sensor_control.pump_water = False
            sensor_control.save()
            return Response(
                {
                    'status_code': 200,                                       
                }, 
                status = status.HTTP_200_OK
            )


class SetDataControlStage3(APIView):
   
    def get(self, request):
            sensor_control = SensorControl.objects.get(user_id=1)
            sensor_control.status = True
            sensor_control.pump_nutrient_a = False
            sensor_control.pump_nutrient_b = False
            sensor_control.pump_water = True
            sensor_control.save()
            return Response(
                {
                    'status_code': 200,                                       
                }, 
                status = status.HTTP_200_OK
            )


class SetDataControlStage4(APIView):
       
    def get(self, request):
            sensor_control = SensorControl.objects.get(user_id=1)
            sensor_control.status = False
            sensor_control.pump_nutrient_a = False
            sensor_control.pump_nutrient_b = False
            sensor_control.pump_water = False
            sensor_control.save()
            return Response(
                {
                    'status_code': 200,                                       
                }, 
                status = status.HTTP_200_OK
            )
            

class PublishControlMessage(APIView):
    permission_classes = (IsAuthenticated,)
    client = mqtt.Client()
    
    def on_connect(self, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def on_message(self, userdata, msg):
        print(msg.payload.decode("utf-8"))

    def get(self, request, format=None):
        
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("sibadaring.com", 1883, 60)
        self.client.publish("reina/input", '{"mixin": "on"}', qos=0, retain=False)
        return redirect('dashboard:garden_control')