from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

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

def statistics_view(request):
    matplotlib.use('Agg')

    # Obtener todas las películas
    allMovies = Movie.objects.all()

    # Gráfico de películas por año
    movieByYear = {}
    for movie in allMovies:
        year = movie.year if movie.year else "None"
        movieByYear[year] = movieByYear.get(year, 0) + 1

    #diseño del gráfico
    bar_positions_year = range(len(movieByYear))
    plt.figure(figsize=(10, 6))
    plt.bar(bar_positions_year, movieByYear.values(), width=0.5, align='center')
    plt.title('Movies by Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions_year, movieByYear.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)
    
    #Guardar la grafica en un objeto BytesIO
    buffer_year = io.BytesIO()
    plt.savefig(buffer_year, format='png')
    buffer_year.seek(0)
    plt.close()

    #convertir la imagen en base64
    img_year = buffer_year.getvalue()
    buffer_year.close()
    graphic_year = base64.b64encode(img_year).decode('utf-8')

    # Gráfico de películas por género
    moviesByGenre = {}
    for movie in allMovies:
        if movie.genre:
            first_genre = movie.genre.split(',')[0].strip()
            moviesByGenre[first_genre] = moviesByGenre.get(first_genre, 0) + 1

    #diseño del gráfico
    bar_positions_genre = range(len(moviesByGenre))
    plt.figure(figsize=(10, 6))
    plt.bar(bar_positions_genre, moviesByGenre.values(), width=0.5, align='center')
    plt.title('Movies by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(bar_positions_genre, moviesByGenre.keys(), rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.3)

    #Guardar la grafica en un objeto BytesIO
    buffer_genre = io.BytesIO()
    plt.savefig(buffer_genre, format='png')
    buffer_genre.seek(0)
    plt.close()
    
    #convertir la imagen en base64
    img_genre = buffer_genre.getvalue()
    buffer_genre.close()
    graphic_genre = base64.b64encode(img_genre).decode('utf-8')

    # Enviar ambas imágenes a la plantilla
    return render(request, 'statistics.html', {'graphic_year': graphic_year, 'graphic_genre': graphic_genre})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})