from django.shortcuts import  redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView
from .forms import ReviewForm
# Create your views here.

from .models import Movie, Category, Actor, Genre

class GenreYear:
    """Жанры и года выходов фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class MoviesView(GenreYear,ListView):
    """Список фильмов """
    model = Movie
    queryset = Movie.objects.filter(draft=False)




class MovieDetailView(GenreYear,DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):
    """Отзывы"""

    def post(self,request,pk):
        form = ReviewForm(request.POST)
        movie= Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url() )


class ActorView(GenreYear,DetailView):
    """Вывод информации о актере"""

    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'