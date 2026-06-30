from django.urls import path
from .views import HomepageView, NoticeView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("about/", NoticeView.as_view(), name="notice"),
]
