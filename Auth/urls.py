from django.urls import path
from Auth import views

urlpatterns = [
    path('', views.get_current_user, name='GetCurrentUser'),
    path('register', views.register_user, name='Register'),
    path('login', views.login_user, name='Login'),
    path('logout', views.logout_user, name='Logout'),
]
