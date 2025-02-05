from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def home(request):
    #return HttpResponse("Welcome")
    #Se cambia porque con render proviene de un html y el httpresponse es un texto que se ingresa aqui mismo
    #return render(request, 'home.html')
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies': movies})

def about(request):
    #return HttpResponse("About Us")
    return render(request, 'about.html')