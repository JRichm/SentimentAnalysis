from django.urls import path
from . import views

urlpatterns = [
    path('testformendpoint/', views.EndpointView),
    path('get_csrf_token/', views.get_csrf_token),
]