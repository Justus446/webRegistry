from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import facilitySerializer, clientSerializer
from .models import Client, Facility


# Create your views here.


# Create and read
@api_view(['GET', 'POST'])
def facility_list(request):
    """
    List all code facilitys, or create a new facility.
    """
    if request.method == 'GET':
        facilities = Facility.objects.all()
        serializer = facilitySerializer(facilities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = facilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def facility_detail(request, pk):
    """
    Retrieve, update or delete a code facility.
    """
    try:
        facility = Facility.objects.get(pk=pk)
    except facility.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = facilitySerializer(facility)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = facilitySerializer(facility, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        facility.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create and read
@api_view(['GET', 'POST'])
def client_list(request):
    """
    List all code clients, or create a new client.
    """
    if request.method == 'GET':
        facilities = Client.objects.all()
        serializer = clientSerializer(facilities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = clientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    """
    Retrieve, update or delete a code client.
    """
    try:
        client = Client.objects.get(pk=pk)

    except client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = clientSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = clientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
