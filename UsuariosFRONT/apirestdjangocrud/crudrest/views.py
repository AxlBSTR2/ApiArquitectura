from django.shortcuts import render
from rest_framework.response import Response
from .models import Servicios
from .serializers import ServiciosSerializer
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def ServiciosLista(request):
    servicios = Servicios.objects.all()
    serializer = ServiciosSerializer(servicios, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ServiciosDetalle(request, pk):
    servicios = Servicios.objects.get(id=pk)
    serializer = ServiciosSerializer(servicios, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ServiciosCrear(request):
    serializer = ServiciosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
def ServiciosActualizar(request, pk):
    servicios = Servicios.objects.get(id=pk)
    serializer = ServiciosSerializer(instance=servicios, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def ServiciosEliminar(request, pk):
    servicios = Servicios.objects.get(id=pk)
    servicios.delete()

    return Response('Eliminado')

