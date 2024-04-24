from django.urls import path
from .views import register, home, CustomLoginView
#* http://127.0.0.1:8000/accounts/register
#* http://127.0.0.1:8000/accounts/home
urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home' ),
    path('login/', CustomLoginView.as_view(), name="login"),
    # path('logout/'),
    # path('home/'),
]
