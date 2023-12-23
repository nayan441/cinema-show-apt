from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid
from .models import Movie, MovieTiming, Seat, Checkout
from .serializers import MovieSerializer,MovieTimingSerializer, SeatSerializer

class NewlyReleasedMovies(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    
class CinemaHallMovies(APIView):
    def get(self, request, movie_id):
        movie_timings = MovieTiming.objects.filter(movie_id=movie_id)
        serializer = MovieTimingSerializer(movie_timings, many=True)
        return Response(serializer.data)


class SeatSelection(APIView):
    def get(self, request, movie_id,cinema_hall_id, movie_timing_id):
        available_seats = Seat.objects.all()
        serializer = SeatSerializer(available_seats, many=True)
        return Response(serializer.data)
    
    def post(self, request, movie_timing_id, cinema_hall_id, movie_id):
            try:
                seat_number = int(request.query_params.get('seat_number'))
            except (ValueError, TypeError):
                return Response({'error': 'Invalid seat number.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                seat = Seat.objects.get(cinema_hall_id=cinema_hall_id, seat_number=seat_number, is_filled=False)
            except Seat.DoesNotExist:
                return Response({'error': 'Seat not available or already reserved.'}, status=status.HTTP_400_BAD_REQUEST)

            reservation_uuid = str(uuid.uuid4())
            seat.is_filled = True
            seat.reservation_uuid = reservation_uuid
            # Checkout.objects.create(reservation_uuid=reservation_uuid)
            seat.save()

            return Response({'message': 'Seat reserved successfully.', 'reservation_uuid':reservation_uuid}, status=status.HTTP_200_OK)



# class Checkout(APIView):
#     def post(self, request, seat_reservation_id):
#             print("seat_reservation_id")
#             print(seat_reservation_id)
#             print("seat_reservation_id")
#             try:
#                 checkout = Checkout.objects.get(reservation_uuid=seat_reservation_id, status=False)
#             except Seat.DoesNotExist:
#                 return Response({'error': 'Seat amount already paid.'}, status=status.HTTP_400_BAD_REQUEST)

#             checkout.status = True
#             checkout.save()
  