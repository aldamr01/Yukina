from app.dashboard.app_views import dashboard
from django.urls import path

app_name = 'dashboard'
urlpatterns = [
    path('', dashboard.garden_monitoring, name='garden_monitoring'),
    path('garden-control', dashboard.garden_control, name='garden_control'),
    path('garden-config', dashboard.garden_configuration, name='garden_configuration'),
    path('account-config', dashboard.account_configuration, name='account_configuration'),
    path('password-config', dashboard.password_configuration, name='password_configuration'),
]
