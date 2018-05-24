from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API viewset for viewing todo instances.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
