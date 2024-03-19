from django.urls import path
from . import views

urlpatterns = [
    path('testformendpoint/', views.EndpointView),
]