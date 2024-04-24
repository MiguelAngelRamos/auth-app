from django.urls import path
from .views import register
#* http://127.0.0.1:8080/register
urlpatterns = [
    path('register/', register, name='register'),
    path('login/'),
    path('logout/'),
    path('home/'),
]
