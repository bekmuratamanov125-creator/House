from rest_framework import serializers
from .models import Region, City, Property, PropertyImage, Review, UserProfile


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['region_name']

class RegionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'region_name', 'region_image']


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [ 'city_name']


class CityDetailSerializer(serializers.ModelSerializer):
    region = RegionListSerializer(read_only=True)
    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_image', 'region']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'age', 'role', 'phone_number', 'avatar']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'property', 'image']


class PropertyListSerializer(serializers.ModelSerializer):
    city = CityListSerializer(read_only=True)
    region = RegionListSerializer(read_only=True)
    class Meta:
        model = Property
        fields = ['id', 'title', 'price', 'city', 'region']

class PropertyDetailSerializer(serializers.ModelSerializer):
    city = CityListSerializer(read_only=True)
    region = RegionListSerializer(read_only=True)
    images = PropertyImageSerializer(many=True,read_only=True,)
    class Meta:
        model = Property
        fields = ['id',  'title', 'description','price','address',
                  'type','is_active','created_date','city','region','images']


class ReviewSerializer(serializers.ModelSerializer):
    buyer = UserProfileSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'property', 'buyer', 'rating',
                  'comment', 'created_date']

