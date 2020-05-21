from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Library
from app.fusioncharts.fusioncharts import FusionCharts
from app.fusioncharts.fusioncharts import FusionTable
from app.fusioncharts.fusioncharts import TimeSeries
import requests

# Application
from app.dashboard.app_models.dashboard import SensorConfig, SensorValue, NutrientValue, SensorCurrentValue


@login_required
def garden_monitoring(request):

   data = '[["01-Feb-11",8866],["02-Feb-11",2174],["03-Feb-11",2084]'
   schema = '[{"name": "Time","type": "date","format": "%d-%b-%y"}, {"name": "Nilai PPM","type": "number"}]'

   fusionTable = FusionTable(schema, data)
   timeSeries = TimeSeries(fusionTable)

   timeSeries.AddAttribute('chart', '{}')
   timeSeries.AddAttribute('caption', '{"text":"Grafik Nutrisi Air"}')
   timeSeries.AddAttribute('subcaption', '{"text":"PPM"}')
   timeSeries.AddAttribute('yaxis', '[{"plot":{"value":"Nilai Sensor PPM"},"format":{"prefix":"$"},"title":"Grafik Nutrisi Air"}]')
   

   # Create an object for the chart using the FusionCharts class constructor
   fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries)
   fcChart2 = FusionCharts("timeseries", "ex2", 700, 450, "chart-2", "json", timeSeries)
   
      
   return  render(request, 'base/dashboard/garden_monitoring.html', {'output' : fcChart.render(),
                                                            'output2' : fcChart2.render()})
   
   
@login_required
def garden_control(request):
   # return render(request, 'base/dashboard/garden_control.html')
   return render(request, 'base/dashboard/garden_control.html')

@login_required
def garden_configuration(request):
   return render(request, 'base/dashboard/garden_configuration.html')

@login_required
def account_configuration(request):
   return render(request, 'base/dashboard/account_configuration.html')

@login_required
def password_configuration(request):
   return render(request, 'base/dashboard/password_configuration.html')