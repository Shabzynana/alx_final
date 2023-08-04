from rest_framework.views import APIView
# # from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from todolist.models import Task
from .serializers import TaskSerializer

# Create your views here.

class TaskApiView(APIView):

    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request):

        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # CREATE A TASK
    def post(self, request):

        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'user_id': request.data.get('user_id')
        }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskIdApiView(APIView):

    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # calling function for a task per id
    def get_task(self, task_id):
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return None


    # GET Task PER ID
    def get(self, request, task_id):

        task = self.get_task(task_id)
        if not task:
            return Response(
                {"res": "task with task_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # UPDATE A PARTICULAR TAsk
    def put(self, request, task_id):

        task = self.get_task(task_id)
        if not task:
            return Response(
                {"res": "Task with task_id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'user_id': request.data.get('user_id')
        }
        serializer = TaskSerializer(instance=task, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # DELETE A PARTICULAR TASK
    def delete(self, request, task_id):

        task = self.get_task(task_id)
        if not task:
            return Response(
                {"res": "Task with task_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        task.delete()
        return Response(
            {"res": "Task deleted!"},
            status=status.HTTP_200_OK
        )
