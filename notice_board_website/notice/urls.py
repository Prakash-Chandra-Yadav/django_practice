from django.urls import path
from .views import HomepageView, NoticeView, AboutView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("notice/", NoticeView.as_view(), name="notice"),
    path("about/", AboutView.as_view(), name="about"),
]
