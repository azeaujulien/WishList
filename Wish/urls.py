from django.urls import path
from Wish import views

urlpatterns = [
    path('create', views.create_wish, name='CreateWish'),
    path('', views.get_wishes, name='GetWishes')
]


