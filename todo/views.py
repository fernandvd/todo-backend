from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet

from .models import Todo 
from .serializer import TodoSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    
    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

