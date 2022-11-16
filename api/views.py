from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

class TaskDetailView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



