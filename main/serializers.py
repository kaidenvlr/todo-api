from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import TaskList, Team, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'is_done', 'date_to', 'date_complete', 'date_created', 'date_updated']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class TeamSerializer(serializers.ModelSerializer):
    members = TeamMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']


class TaskListSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = TaskList
        fields = ['id', 'name', 'color', 'team', 'tasks']
