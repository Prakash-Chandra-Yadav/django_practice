from django.shortcuts import render


# Create your views here.
def home_page_view(request):
    """returns the view contained in the homepage"""
    return render(request, "home.html")
