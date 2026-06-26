from django.http import HttpResponse


# Create your views here.
def home_Page(request):
    return HttpResponse("Hello, Prakash")
