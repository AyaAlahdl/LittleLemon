from django.db import models
from django.utils import timezone


class Booking(models.Model):
    name = models.CharField(max_length=255, default='Booking')
    no_of_guests = models.IntegerField(default=6)
    booking_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name}: {self.booking_date}'


class Menu(models.Model):
    title = models.CharField(max_length=255, default='menu')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.title}: ${self.price:.2f}'
     
#class MenuItem(models.Model):
   #title = models.CharField(max_length=255)
   #price = models.DecimalField(max_digits=6, decimal_places=2)
   #inventory = models.SmallIntegerField()

  # def get_item(self):
   #   return f'{self.title} : {str(self.price)}'