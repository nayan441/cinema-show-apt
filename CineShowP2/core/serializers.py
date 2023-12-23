from rest_framework import serializers
from .models import Movie, MovieTiming, Timings, Seat, CinemaHall


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['seat_number', 'is_filled']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'genre', 'ratings', 'votes', 'screen']

class CinemaHallSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = CinemaHall
        fields = ['id', 'name', 'seats']

class TimingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timings
        fields = ['id','timing']

class MovieTimingSerializer(serializers.ModelSerializer):
    cinema_hall = CinemaHallSerializer()
    timing = TimingsSerializer()
    class Meta:
        model = MovieTiming
        fields = ['movie',  "cinema_hall", 'timing',]




