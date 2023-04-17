from rest_framework import serializers
from webapp.models import Task, Project, Type, Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']
        read_only_fields = ['id']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']
        read_only_fields = ['id']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'author', 'start_date', 'end_date']
        read_only_fields = ['author']


class TaskSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=True, read_only=True)
    type = TypeSerializer(many=True, read_only=True)
    project = ProjectSerializer(many=False, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'summary', 'description', 'project', 'status', 'type', 'created_at', 'updated_at']
        read_only_fields = ['project', 'status', 'type']

