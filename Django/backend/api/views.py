from django.contrib.auth.models import User, Group
from api.models import Fires, Weather, DataFire
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer, FiresSerializer, FileUploadSerializer, DataFireSerializer
from rest_framework.response import Response
from rest_framework import status
import requests
from django.shortcuts import render
import io, csv, pandas as pd
from datetime import datetime
from math import pi
from django.db import connection

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
    queryset = Fires.objects.all()
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

class DataFireViewSet(viewsets.ModelViewSet):
    serializer_class = DataFireSerializer
    queryset = DataFire.objects.all()

    def get_queryset(self):
        if self.request.GET.get('lat') and self.request.GET.get('lng'):
            user_lat = self.request.GET.get('lat')
            user_lng = self.request.GET.get('lng')
            raio = 1000 * 10
            #cursor = connection.cursor()
            #cursor.execute(f'''SELECT * FROM public.api_datafire LIMIT 5''')
            #print(cursor.fetchone())
            queryset = DataFire.objects.raw(f"SELECT * FROM api_datafire AS api WHERE {raio} > (((acos(sin(({user_lat}*{pi}/180)) * sin((api.latitude*{pi}/180))+cos(({user_lat}*{pi}/180)) * cos((api.latitude*{pi}/180)) * cos((({user_lng} - api.longitude)*{pi}/180))))*180/{pi})*60*1.1515*1.609344)*1000 LIMIT 10")
        else:
            print('teste')
            queryset = DataFire.objects.none()
        
        return queryset

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = DataFire(
                       latitude = row['latitude'],
                       longitude= row["longitude"],
                       bright_ti4= row['bright_ti4'],
                       scan= row["scan"],
                       track= row["track"],
                       acq_date = row['acq_date'],
                       acq_time= row["acq_time"],
                       satellite= row['satellite'],
                       instrument= row["instrument"],
                       confidence= row["confidence"],
                       version = row['version'],
                       bright_ti5= row["bright_ti5"],
                       daynight= row['daynight'],
                       type= row["type"]
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = DataFire(
                       latitude = row['latitude'],
                       longitude= row["longitude"],
                       bright_ti4= row['bright_ti4'],
                       scan= row["scan"],
                       track= row["track"],
                       acq_date = datetime.strptime(row['acq_date'], '%Y-%m-%d').strftime('%Y-%m-%d'),
                       acq_time= row["acq_time"],
                       satellite= row['satellite'],
                       instrument= row["instrument"],
                       confidence= row["confidence"],
                       version = row['version'],
                       bright_ti5= row["bright_ti5"],
                       frp = row["frp"],
                       daynight= row['daynight'],
                       type= row["type"]
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
