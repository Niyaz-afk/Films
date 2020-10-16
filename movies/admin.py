from django.contrib import admin
from .models import Category, Actor, Reviews, Rating, RatingStar, Movie, MovieShots, Genre
# Register your models here.
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Reviews)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Genre)


