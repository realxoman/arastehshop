from django.urls import path
from .views import *
app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', UserCreateView.as_view(), name="register")
]