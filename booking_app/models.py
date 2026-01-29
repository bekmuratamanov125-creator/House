from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Region(models.Model):
    region_name = models.CharField(max_length=64)
    region_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.region_name



class City(models.Model):
    city_name = models.CharField(max_length=100)
    city_image = models.ImageField(upload_to='images/')

    def str(self):
        return self.city_name


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(60)],
                                                       null=True,blank=True)
    ROLE_CHOICES = (
        ('Seller', 'Seller'),
        ('Buyer', 'Buyer'),
        ('Admin', 'Admin'),

    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')
    phone_number = PhoneNumberField(null=True,blank=True, default='')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def str(self):
        return f'{self.first_name} {self.last_name} {self.role}'


class Room(models.Model):
    room_number = models.CharField(max_length=64)
    room_image = models.ImageField(upload_to='images/')


class Property(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    TYPE_CHOICES = (
    ('Floor', 'Floor'),
    ('House', 'House'),
    ('Apartment', 'Apartment'),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=64, default='Floor')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE,related_name='properties_in_city')
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    district = models.ForeignKey(City, on_delete=models.CASCADE, related_name='properties_in_district')
    address = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    floor = models.PositiveSmallIntegerField()
    documents = models.TextField()
    condition = models.TextField()
    total_floor = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)



class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating