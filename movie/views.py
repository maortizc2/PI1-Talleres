from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Welcome")
    #Se cambia porque con render proviene de un html y el httpresponse es un texto que se ingresa aqui mismo
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'Greg Lim'})

def about(request):
    return HttpResponse("About Us")