from django.contrib.auth.models import User, Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
