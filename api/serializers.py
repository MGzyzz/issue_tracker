from rest_framework import serializers
from rest_framework.views import APIView
from issue_tracker.models import Task, project


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['summary', 'description',  'status', 'type', 'time_of_create', 'update_time', 'project', 'is_deleted']


class TaskDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']


