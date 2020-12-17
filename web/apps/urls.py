

from django.urls import path, include
import apps
from apps import views
urlpatterns = [
    path('', views.home, name ="home"),
]