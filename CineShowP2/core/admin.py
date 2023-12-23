from django.contrib import admin

from .models import Movie,CinemaHall, MovieTiming, Timings, Seat

admin.site.register(Movie)
admin.site.register(CinemaHall)
admin.site.register(MovieTiming)
admin.site.register(Timings)
admin.site.register(Seat)