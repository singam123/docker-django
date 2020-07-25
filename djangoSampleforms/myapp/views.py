from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("Hello Welcome to you first ever Django web page :)")

