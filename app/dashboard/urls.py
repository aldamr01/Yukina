from app.dashboard.app_views.views import chart
from django.urls import path

app_name = 'dashboard'
urlpatterns = [
    path('', chart, name='index')
]
