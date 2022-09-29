from rest_framework import serializers

from .models import Facility, Client


class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class facilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'



