from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .models import Task
from django.shortcuts import get_object_or_404, render
import json


def home(request):
    return render('home.html', {})

@api_view(['GET'])
def get_all_tasks(request):
    print(request.method)
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, 200)


@api_view(['GET'])
def get_task(request, pk):
    print(request.method)
    task = get_object_or_404(Task, pk=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data, 200)


@api_view(['POST'])
def create_task(request):
    task = Task(
        text = request.data['text'],
        date = request.data['date'],
        reminder = request.data['reminder'],
    )
    task.save()
    serializer = TaskSerializer(task, many=False)
    return Response({}, 200)

@api_view(['DELETE'])
def delete_task(request, taskID):
    task = get_object_or_404(Task, pk=taskID)
    task.delete()
    return Response({'detail': 'task successfully deleted'}, 200)

@api_view(['PUT'])
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.reminder = not task.reminder
    task.save()
    return Response(TaskSerializer(task, many=False).data, 200)