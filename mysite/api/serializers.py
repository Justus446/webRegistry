from rest_framework import serializers

from .models import Patient, Role, Person, Item


class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class roleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
