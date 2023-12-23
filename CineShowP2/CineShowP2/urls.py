
from django.contrib import admin
from django.urls import path
from core.views import NewlyReleasedMovies,CinemaHallMovies, SeatSelection, Checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newly-released-movies/', NewlyReleasedMovies.as_view(), name='newly-released-movies'),
    path('cinema-hall-movies/<int:movie_id>/', CinemaHallMovies.as_view(), name='cinema-hall-movies'),
    path('seat-selection/<int:movie_id>/<int:cinema_hall_id>/<int:movie_timing_id>', SeatSelection.as_view(), name='seat-selection'),
    # path('checkout/<str:seat_reservation_id>', Checkout.as_view(), name='checkout'),

]