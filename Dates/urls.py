from django.urls import path
from Dates import views

urlpatterns = [
    path('', views.get_events, name='GetEvents'),
]
