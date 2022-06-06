from webbrowser import get
from django.shortcuts import render,redirect,get_object_or_404
from .forms import MovieForm
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    #context 
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    elif request.method == 'GET':
        form = MovieForm()
        context = {
            'form': form,
        }
        return render(request, 'movies/create.html', context)

def detail(request, id):
    movie = get_object_or_404(Movie,pk=id)
    context ={
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

def update(request, id):
    movie = get_object_or_404(Movie,pk=id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance= movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    elif request.method == 'GET':
        form = MovieForm(instance= movie)
        context = {
            'form': form,
        }
        return render(request, 'movies/update.html', context)
    
def delete(request, id):
    movie = get_object_or_404(Movie,pk=id)
    movie.delete()
    return redirect('movies:index')