import graphene 
from graphene_django import DjangoObjectType
from django.db.models import Q

from todo.models import Todo 


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo 

class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)
    todo_search = graphene.List(TodoType, search=graphene.String())

    def resolve_todos(self, info, **kwargs):
        return Todo.objects.all()
    
    def resolve_todo_search(self, info, **kwargs):
        search = kwargs.get('search', None)
        if search:
            return Todo.objects.filter(Q(titulo__icontains=search) | Q(descripcion__icontains=search))
        return Todo.objects.all()
    
schema = graphene.Schema(query=Query)
