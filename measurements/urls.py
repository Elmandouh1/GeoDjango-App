from django.urls import path 
from . import views 

app_name = 'measurements'

urlpatterns = [
    path('', views.calcDistanceView, name='calc_distance'),
]
