from django.urls import path
from .views import home_Page

urlpatterns = [
    path("", home_Page),
]
