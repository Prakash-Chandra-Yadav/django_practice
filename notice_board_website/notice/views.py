from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import message


# Create your views here.
class HomepageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["company_name"] = "ABC pvt.ltd"
        context["company_type"] = "finance"
        return context


class NoticeView(ListView):
    model = message
    template_name = "notice.html"
