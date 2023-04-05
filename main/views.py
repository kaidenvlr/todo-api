from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from main.models import Task, TaskList
from main.serializers import TaskSerializer, TaskListSerializer


class TaskViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class TaskListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = TaskList.objects.all()
        serializer = TaskListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TaskList.objects.all()
        task_list = get_object_or_404(queryset, pk=pk)
        serializer = TaskListSerializer(task_list)
        return Response(serializer)
