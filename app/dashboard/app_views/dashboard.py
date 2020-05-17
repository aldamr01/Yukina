from django.shortcuts import render
from django.http import HttpResponse

# Include the fusioncharts.py file which has required functions to embed the charts in html page
from app.fusioncharts.fusioncharts import FusionCharts
from app.fusioncharts.fusioncharts import FusionTable
from app.fusioncharts.fusioncharts import TimeSeries
import requests

# Loading Data and schema from a Static JSON String url
# The chart method is defined to load chart data from an JSON string.

def garden_monitoring(request):

   data = '[["01-Feb-11",8866],["02-Feb-11",2174],["03-Feb-11",2084],["04-Feb-11",1503],["05-Feb-11",4928],["06-Feb-11",4667],["07-Feb-11",1064],["08-Feb-11",851],["09-Feb-11",7326]]'
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

   # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
   return  render(request, 'base/dashboard/garden_monitoring.html', {'output' : fcChart.render(),
                                                            'output2' : fcChart2.render()})
   

def garden_control(request):
   # return render(request, 'base/dashboard/garden_control.html')
   return render(request, 'base/authentication/garden_control.html')

def garden_configuration(request):
   return render(request, 'base/dashboard/garden_configuration.html')

def account_configuration(request):
   return render(request, 'base/dashboard/account_configuration.html')

def password_configuration(request):
   return render(request, 'base/dashboard/password_configuration.html')