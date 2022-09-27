from django.shortcuts import render
from rest_framework import viewsets
from .serializers import patientSerializer, personSerializer, itemSerializer, roleSerializer
from .models import Patient, Person, Item, Role


# Create your views here.


class patient_view(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('first_name')
    serializer_class = patientSerializer


class person_view(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('first_name')
    serializer_class = personSerializer


class item_view(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('name')
    serializer_class = itemSerializer


class role_view(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('name')
    serializer_class = roleSerializer
