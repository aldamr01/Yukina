from django.urls import path
from app.authentication.app_views import authentication


app_name = 'authentication'
urlpatterns = [
    path('signin', authentication.signin, name='signin'),
    path('signout', authentication.signout, name='signout')
]