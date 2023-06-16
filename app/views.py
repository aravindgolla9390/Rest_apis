from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


@api_view(['GET'])
def bookdata(request):
    book=Book.objects.all()
    serializer=BookSerializers(book,many=True)
    return Response(serializer.data)



@api_view(['POST'])
def addingBookdata(request):
    book=Book.objects.all()
    serializer=BookSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['PUT'])
def updatingBookdata(request,id):
    book=Book.objects.get(id=id)
    serializer=BookSerializers(instance=book,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletingBookdata(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return Response(" REcord deleted susessfully")