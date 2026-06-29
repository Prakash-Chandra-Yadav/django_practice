from django.urls import path
from .views import home_page_view, AboutpageView

urlpatterns = [path("", home_page_view), path("about/", AboutpageView.as_view())]
