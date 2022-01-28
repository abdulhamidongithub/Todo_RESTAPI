from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from todoapp.models import Todo
from todoapp.serializers import TodoSerializer

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]



