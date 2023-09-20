from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from issue_tracker.models import Task
from .serializers import TaskDetailSerializers, TaskUpdateSerializers

# Create your views here.


class TaskDetailView(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskDetailSerializers(task)
            return JsonResponse(serializer.data, status=200)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)

class TaskUpdateView(APIView):
    def put(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return JsonResponse({'success': 'Not Work'}, status=404)
        serializer = TaskUpdateSerializers(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

class TaskDeleteView(APIView):
    def delete(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
            task.delete()
            return JsonResponse({'message': 'Task deleted successfully'}, status=204)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)