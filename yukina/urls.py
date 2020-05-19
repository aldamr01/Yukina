# Django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.dashboard.urls', namespace='dashboard')),
    path('', include('app.authentication.urls', namespace='authentication')),
]
