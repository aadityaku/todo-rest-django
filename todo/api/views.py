
from django.shortcuts import render
from .serializers import TodoSerializer,MyTokenObtainPairSerializer
from rest_framework import generics
from .models import Todo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
# Create your views here.
# class TodoList(generics.ListAPIView):
#     queryset=Todo.objects.all()
#     serializer_class=TodoSerializer
@api_view(['GET'])
def todolist(r):
    task=Todo.obj.all()
    serializer=TodoSerializer(task,many=True)

    return Response(serializer.data)


@api_view(['GET'])
def todolistDetails(r,pk):
    task=Todo.obj.get(id=pk)
    serializer=TodoSerializer(task,many=False)

    return Response(serializer.data)
@api_view(['POST'])
def createTodo(r):
    serializer=TodoSerializer(data=r.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateView(r,id):
    task=Todo.objects.get(pk=id)
    serializer=TodoSerializer(instance=task,data=r.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteTodo(r,id):
    task=Todo.objects.get(id=id)
    task.delete()
    return Response("data is deleted succecfully")

class MyObtainTokenPairView(TokenObtainPairView):
    permission_clases=(AllowAny)
    serializer_class=MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_clases=(AllowAny)
    serializer_class=RegisterSerializer

