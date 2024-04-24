from django.urls import path
from .views import register, home
#* http://127.0.0.1:8080/accounts/register
urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home' )
    # path('login/'),
    # path('logout/'),
    # path('home/'),
]
