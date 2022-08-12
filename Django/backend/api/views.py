from django.contrib.auth.models import User, Group
from api.models import Fires, Weather
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, FiresSerializer
from rest_framework.response import Response
from rest_framework import status
import requests


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class FiresViewSet(viewsets.ModelViewSet):
    """Metodo responsavel por criar a queimada e consultar a previsão do tempo"""
    queryset = Fires.objects.none()
    serializer_class = FiresSerializer

    def perform_create(self, serializer):
        lon = self.request.data.get('latitude')
        lat = self.request.data.get('longitude')
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=pt_br&APPID=1310621859aea3be3e21c21294c71cf1"
        data_weather = requests.get(weather_url).json()
        weather = Weather.objects.create(temp=data_weather['main']['temp'],
                                        feels_like=data_weather['main']['feels_like'],
                                        humidity=data_weather['main']['humidity'],
                                        pressure=data_weather['main']['pressure'],
                                        dew_point=0,
                                        wind_speed=data_weather['wind']['speed'],
                                        wind_gust=data_weather['wind']['gust'],
                                        wind_deg=data_weather['wind']['deg'])
        weather.save()
        if serializer.is_valid():
            serializer.save(weather=weather, city='teste', state='teste', country='teste')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        self.perform_create(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
