from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoItem
from .serializers import TodoItemSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'todo_form.html')

@api_view(['GET'])
def todo_list_api(request):
    todos = TodoItem.objects.all()
    serializer = TodoItemSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def todo_create_api(request):
    serializer = TodoItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def todo_update_api(request, id):
    try:
        todo = TodoItem.objects.get(id=id)
    except TodoItem.DoesNotExist:
        return Response(status=404)

    serializer = TodoItemSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def todo_delete_api(request, id):
    try:
        todo = TodoItem.objects.get(id=id)
    except TodoItem.DoesNotExist:
        return Response(status=404)

    todo.delete()
    return Response(status=204)
        
        