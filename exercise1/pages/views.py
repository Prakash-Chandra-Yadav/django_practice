from django.shortcuts import render


# Create your views here.
def home_page_view(request):
    """returns the view contained in the homepage"""
    context = {
        "skills": ["python", "django", "java", ".net", "sql"],
        "gteetings": "ThAnKs For ViSITing My WEbSiTe",
    }
    return render(request, "home.html", context)
