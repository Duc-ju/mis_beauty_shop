from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'gender', 'photoUrl', 'displayName']


class CustomerCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = Customer.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            displayName=validated_data['displayName'],
            email=validated_data['email']
        )
        return user

    class Meta:
        model = Customer
        fields = ['id', 'username', 'password', 'email', 'displayName']
