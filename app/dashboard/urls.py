# Django
from app.dashboard.app_views import dashboard
from django.urls import path, include
from django.views.generic import TemplateView

# Application
from app.dashboard.api import dashboard as api
from app.dashboard.app_views import dashboard

app_name = 'dashboard'
urlpatterns = [
    path('', dashboard.garden_monitoring, name='garden_monitoring'),
    path('garden-control', dashboard.garden_control, name='garden_control'),
    path('garden-config', dashboard.garden_configuration, name='garden_configuration'),
    path('account-config', dashboard.account_configuration, name='account_configuration'),
    path('password-config', dashboard.password_configuration, name='password_configuration'),
    path('start-mixin', dashboard.start_mixin, name='start_mixin'),
    
    path('api/', include(([
        path('v1/', include(([
            path('currentvalue/', api.CurrentSensorValue.as_view(), name="currentvalue"),
            path('sensorcontrol/', api.GetDataControl.as_view(), name="sensorcontrol"),
            path('setdatacontrol1/', api.SetDataControlStage1.as_view(), name="setdatacontrol1"),
            path('setdatacontrol2/', api.SetDataControlStage2.as_view(), name="setdatacontrol2"),
            path('setdatacontrol3/', api.SetDataControlStage3.as_view(), name="setdatacontrol3"),
            path('setdatacontrol4/', api.SetDataControlStage4.as_view(), name="setdatacontrol4"),
        ], 'v1'), namespace='v1')),
    ], 'api'), namespace='api')),
    
    path('ied-mubarak.exe', TemplateView.as_view(template_name='base/index.html'))
]
