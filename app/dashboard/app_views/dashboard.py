from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Library
from app.fusioncharts.fusioncharts import FusionCharts
from app.fusioncharts.fusioncharts import FusionTable
from app.fusioncharts.fusioncharts import TimeSeries
import requests

# Application
from app.dashboard.app_models.dashboard import SensorConfig, SensorValue, NutrientValue, SensorCurrentValue, SensorControl
from app.dashboard.app_forms.dashboard import SensorConfigUpdateForm

@login_required
def garden_monitoring(request):

   data_tds = []
   data_ph = []
   current_value = get_object_or_404(SensorCurrentValue, user_id=request.user.id)
   config_value = get_object_or_404(SensorConfig, user_id=request.user.id)
   nutrient_value = get_object_or_404(NutrientValue, user_id=request.user.id)
   
   for datasensor in SensorValue.objects.filter(user_id=request.user.id).order_by('-created_at'):
      data_tds.append([datasensor.created_at.strftime("%d-%m-%y %H:%M:%S"),datasensor.value_tds])
      data_ph.append([datasensor.created_at.strftime("%d-%m-%y %H:%M:%S"),datasensor.value_ph])
      
   schema_tds = '[{"name": "Time","type": "date","format": "%d-%m-%y %H:%-M:%S"}, {"name": "Nilai PPM","type": "number"}]'
   schema_ph = '[{"name": "Time","type": "date","format": "%d-%m-%y %H:%-M:%S"}, {"name": "Nilai pH","type": "number"}]'

   table_tds = FusionTable(schema_tds, str(data_tds))
   table_ph = FusionTable(schema_ph, str(data_ph))
   timeSeries_tds = TimeSeries(table_tds)
   timeSeries_ph = TimeSeries(table_ph)

   timeSeries_tds.AddAttribute('chart', '{}')
   timeSeries_tds.AddAttribute('caption', '{"text":"Grafik Nutrisi Air"}')
   timeSeries_tds.AddAttribute('subcaption', '{"text":"PPM"}')
   timeSeries_tds.AddAttribute('yaxis', '[{"plot":{"value":"Nilai Sensor PPM"},"format":{"prefix":"$"},"title":"Grafik Nutrisi Air", "type":"log"}]')
   
   timeSeries_ph.AddAttribute('chart', '{}')
   timeSeries_ph.AddAttribute('caption', '{"text":"Grafik Keasaman Air"}')
   timeSeries_ph.AddAttribute('subcaption', '{"text":"pH"}')
   timeSeries_ph.AddAttribute('yaxis', '[{"plot":{"value":"Nilai Sensor pH"},"format":{"prefix":"$"},"title":"Grafik Keasaman Air", "type":"log"}]')
   

   # Create an object for the chart using the FusionCharts class constructor
   fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries_tds)
   fcChart2 = FusionCharts("timeseries", "ex2", 700, 450, "chart-2", "json", timeSeries_ph)
   
      
   return render(
      request, 
      'base/dashboard/garden_monitoring.html', 
      {
         'output' : fcChart.render(), 
         'output2' : fcChart2.render(),
         'current_value': current_value,
         'config_value': config_value,
         'nutrient_value': nutrient_value,
      }
   )
   
   
@login_required
def garden_control(request):
   nutrient_value = get_object_or_404(NutrientValue, user_id=request.user.id)
   sensor_control = get_object_or_404(SensorControl, user_id=request.user.id)
   return render(
      request, 
      'base/dashboard/garden_control.html',
      {
         'nutrient_value': nutrient_value,
         'sensor_control': sensor_control
      }
   )

@login_required
def garden_configuration(request):   
   sensor_config = get_object_or_404(SensorConfig, user_id=request.user.id)
   form = SensorConfigUpdateForm(request.POST or None, instance=sensor_config)
   if request.method == 'POST':
      if form.is_valid():
         form.save()
         messages.add_message(request, messages.SUCCESS, 'berhasil mengubah data konfigurasi') 
      else:        
         messages.add_message(request, messages.WARNING, 'gagal mengubah data konfigurasi')
      return redirect('dashboard:garden_configuration')
   
   return render(
      request, 
      'base/dashboard/garden_configuration.html',
      {
         'sensor_config': sensor_config,
         'form': form
      }
   )

@login_required
def account_configuration(request):
   return render(request, 'base/dashboard/account_configuration.html')

@login_required
def password_configuration(request):
   return render(request, 'base/dashboard/password_configuration.html')

@login_required
def start_mixin(request):
   sensor_control = SensorControl.objects.get(user_id=request.user.id)
   if sensor_control.status is True:
      messages.add_message(request, messages.WARNING, 'pencampur sedang menyala! tunggu beberapa saat lagi')
   else:
      sensor_control.status = True
      sensor_control.pump_nutrient_a = False
      sensor_control.pump_nutrient_b = False
      sensor_control.pump_water = False
      sensor_control.save()
      messages.add_message(request, messages.SUCCESS, 'pencampur berhasil dinyalakan!')
      
   return redirect('dashboard:garden_control')