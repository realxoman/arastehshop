from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', HomePage.as_view(), name="HomePage"),
    path('pages/<str:slug>/', PageView.as_view(), name="pages"),
]