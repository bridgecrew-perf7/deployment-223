from django.urls import path
from . import views

app_name = 'PortFolio'

urlpatterns = [
    path('', views.home, name='port_home')

]
