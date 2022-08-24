from django.contrib.auth.models import User, Group
from api.models import Fires, Weather
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class FiresSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        post = Fires.objects.create(**validated_data)  # saving post object
        return post

    class Meta:
        model = Fires
        fields = ('latitude', 'longitude', 'biome', 'country', 'state', 'city', 'weather')
        read_only_fields = ('country', 'state', 'city', 'weather')
