from django.db import models
from django.utils.timezone import now
from datetime import datetime


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    dealership = models.IntegerField()

    CAR = 'car'
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    SPORT = 'sport'
    TYPE_CHOICES = [
        (SEDAN,'Sedan'),
        (SUV,'SUV'),
        (WAGON,'Station Wagon'),
        (SPORT,'Sport')
        ]

    car_type = models.CharField(max_length = 20, choices=TYPE_CHOICES)
    year = models.DateField()

    def __str__(self):
        return self.year.strftime("%Y") + " " + self.make.name + " " + self.name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, state, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        self.state = state
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id

    def __str__(self):
        return "Review: " + self.review