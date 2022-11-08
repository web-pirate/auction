from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    CATEGORY = [
        ('vehicles', "vehicles"),
        ('jewelry', "jewelry"),
        ('watch', "watch"),
        ('Electronics', "Electronics"),
        ('Sports', "sports"),
        ('Real Estate', "Real Estate"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="auctionItems")
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="userProfile")
    dob = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    addhar = models.CharField(max_length=50)
    

    def __str__(self):
        return self.user


class Bid(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    amout = models.FloatField()
