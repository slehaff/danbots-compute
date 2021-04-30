from django.urls import path
from api import views

urlpatterns = [
    path('scan3d', views.scan3d),
    path('stop3d', views.scan3d),
]
