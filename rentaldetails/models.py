from django.conf import settings
from django.db import models


class Rental(models.Model):
    id = models.AutoField(primary_key=True)
    Name_of_rental = models.CharField(max_length=255)
    Image_url = models.CharField(max_length=2090)
    Type_of_rental = models.CharField(max_length=256)
    Total_no_of_units = models.IntegerField()
    Rent = models.FloatField()
    Name = models.CharField(max_length=255)
    Image_url1 = models.CharField(max_length=2090)
    Deposit = models.FloatField()
    Location = models.CharField(max_length=2000)
    Floors = models.CharField(max_length=256)
    Walls = models.CharField(max_length=256)
    Roof = models.CharField(max_length=256)
    Bathroom = models.CharField(max_length=256)
    Electricity = models.CharField(max_length=256)
    Water = models.CharField(max_length=500)
    Contacts = models.CharField(max_length=350)

    def __str__(self):
        return self.Name_of_rental


class BookRental(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    Name_of_rental = models.CharField(max_length=255)

    def __str__(self):
        return self.Name_of_rental


class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rentals = models.ManyToManyField(BookRental)
    start_date = models.DateTimeField(auto_now_add=True)
    booked_date = models.DateTimeField()
    booked = models.BooleanField(default=False)

    def __str__(self):
        return self.Name_of_rental
