from rest_framework import viewsets, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Region, City, Property, PropertyImage, Review, UserProfile
from .serializers import RegionListSerializer, RegionDetailSerializer, CityListSerializer, CityDetailSerializer, PropertyListSerializer, PropertyDetailSerializer, PropertyImageSerializer, \
     ReviewSerializer, UserProfileSerializer
from .poginations import PropertyPagination

class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['region_name']
    ordering_fields = ['region_name']


class RegionDetailAPIView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer


class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['city_name']
    ordering_fields = ['city_name']

class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.filter(is_active=True).order_by('-created_date')
    serializer_class = PropertyListSerializer
    pagination_class = PropertyPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'city', 'region', 'type', 'price']
    search_fields = ['title', 'description', 'address']
    ordering_fields = ['price', 'created_date']


class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.filter(is_active=True)
    serializer_class = PropertyDetailSerializer



class PropertyImageViewSet(ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['property', 'seller', 'rating']
    search_fields = ['comment']
    ordering_fields = ['rating', 'created_date']

    def get_queryset(self):
        return Review.objects.all().order_by('-created_date')

    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)


