from api.models import DataFire
from rest_framework import viewsets
from api.serializers import FileUploadSerializer, DataFireSerializer
from rest_framework.response import Response
from rest_framework import status
import io, csv, pandas as pd
from datetime import datetime
from math import pi

class DataFireViewSet(viewsets.ModelViewSet):
    serializer_class = DataFireSerializer
    queryset = DataFire.objects.all()

    def get_queryset(self):
        if self.request.GET.get('lat') and self.request.GET.get('lng'):
            user_lat = self.request.GET.get('lat')
            user_lng = self.request.GET.get('lng')
            raio = self.request.GET.get('raio')
            queryset = DataFire.objects.raw(f"SELECT * FROM api_datafire AS api WHERE {1000 * int(raio)} > (((acos(sin(({user_lat}*{pi}/180)) *"
                                             " sin((api.latitude*{pi}/180))+cos(({user_lat}*{pi}/180)) * "
                                             "cos((api.latitude*{pi}/180)) * cos((({user_lng} - api.longitude)*{pi}/180))))"
                                             "*180/{pi})*60*1.1515*1.609344)*1000 LIMIT 10")
        else:
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
