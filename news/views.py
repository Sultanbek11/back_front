from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NewsSerializer
from .models import News


@api_view(['GET'])
def list_view(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail_view(request, id):
    detail_new = News.objects.get(id=id)
    serializer = NewsSerializer(detail_new)
    return Response(serializer.data)


@api_view(['POST'])
def create_view(request):
    serializer = NewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def update_view(request, id):
    object_ = News.objects.get(id=id)
    serializer = NewsSerializer(instance=object_, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_view(request, id):
    object_ = News.objects.get(id=id)
    object_.delete()
    return Response({'text': 'this object is deleted'})
