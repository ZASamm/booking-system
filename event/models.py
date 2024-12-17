from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField()
    available_tickets = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name


class BookingTable(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    numberOfTickets = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} booking for {self.event.name}'
