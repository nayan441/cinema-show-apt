from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    ratings = models.FloatField(null=True, blank=True)
    votes = models.IntegerField(null=True, blank=True)
    screen = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.name)
    
class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    total_seats = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.name)
    
class Timings(models.Model):
    timing_choices = [
    ('06:00', '6:00'),
    ('09:00', '9:00'),
    ('12:00', '12:00'),
    ('15:00', '15:00'),
    ('18:00', '18:00'),
    ('21:00', '21:00'),
    ]
    timing = models.CharField(max_length=222, choices=timing_choices, null=True, blank=True)

    def __str__(self):
        return str(self.timing)
    

class MovieTiming(models.Model):
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    timing = models.ForeignKey(Timings, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.cinema_hall} -- {self.timing} -- {self.movie}"

    class Meta:
        unique_together = ('timing', 'cinema_hall')


    
class Seat(models.Model):
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    is_filled = models.BooleanField(default=False)
    reservation_uuid = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        # Ensure a CinemaHall has a maximum of 10 seats
        unique_together = ('cinema_hall', 'seat_number')
        constraints = [
            models.CheckConstraint(check=models.Q(seat_number__lte=10), name='max_10_seats')
        ]
    def __str__(self):
        return f"{self.cinema_hall} -- {self.seat_number} -- {self.is_filled}"

class Checkout(models.Model):
    reservation_uuid = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=False)