from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home_page_view(request):
    """returns the view contained in the homepage"""
    context = {
        "skills": ["python", "django", "java", ".net", "sql"],
        "gteetings": "ThAnKs For ViSITing My WEbSiTe",
        "degree": "Bsc Hons in computing",
        "college": "the british college",
        "gpa": "4.00",
    }
    return render(request, "home.html", context)


# create the child class if the Tempelate view
class AboutpageView(TemplateView):
    """initialize the attribute if the view"""

    template_name = "about.html"
