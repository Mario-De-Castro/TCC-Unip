from django.contrib.auth.models import User, Group
from api.models import Fires
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
    class Meta:
        model = Fires
        fields = '__all__'
