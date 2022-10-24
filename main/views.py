import base64
import json

from django.shortcuts import render
from django.forms.models import model_to_dict
import pickle
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, \
    RetrieveAPIView, GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import *
from main.serializers import *


class Index(TemplateView):
    template_name = './main/index.html'


class CreateUser(APIView):
    parser_classes = [MultiPartParser, FormParser]

    @staticmethod
    def get_initials(first_name, last_name):
        initials = first_name.upper()[0] + last_name.upper()[0]
        if len(CustomUser.objects.filter(initials=initials)) >= 1:
            initials = first_name.upper()[0] + last_name.upper()[0] + last_name[1]
        return initials

    def post(self, request):
        request.data['initials'] = self.get_initials(request.data['first_name'], request.data['last_name'])
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColumnANDListApi(APIView):

    def get(self, request, *args, **kwargs):
        column_queryset = TableColumns.objects.all()
        task_queryset = Tasks.objects.all()
        column_serializer_class = ColumnSerializer
        column_serializer = column_serializer_class(column_queryset, many=True)
        task_serializer_class = TasksSerializer
        task_serializer = task_serializer_class(task_queryset, many=True)
        response_results = {
            "columns": column_serializer.data,
            "tasks": task_serializer.data,
        }
        return Response(response_results)


class AddColumnAPIView(APIView):
    def post(self, request):
        serializer = ColumnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddTaskAPI(APIView):
    def post(self, request):
        task_serializer = TasksSerializer(data=request.data)
        task_serializer.is_valid(raise_exception=True)
        task_serializer.save()
        task_id = Tasks.objects.get(id=task_serializer.data['id']).id
        column = TableColumns.objects.get(id=request.data['column'])

        order = column.order
        order.append(task_id)
        column.order = order
        column.save()

        resp ={
            'task': task_serializer.data,
            'order': order
        }
        return Response(resp, status=status.HTTP_201_CREATED)



class DNDView(APIView):

    def post(self, request):
        col_to_data = request.data['colTo']
        task_data = request.data['cart']
        task = Tasks.objects.get(id=task_data['id'])
        task.column_id = col_to_data['id']
        task.save()
        col_from_data = request.data['colFrom']
        column_from = TableColumns.objects.get(id=col_from_data['id'])
        column_from.order = col_from_data['orderFrom']
        column_from.save()
        column_to = TableColumns.objects.get(id=col_to_data['id'])
        column_to.order = col_to_data['orderTo']
        column_to.save()
        return Response({"posts": 1})










class ColumnListApi(viewsets.ModelViewSet):
    queryset = TableColumns.objects.all()
    serializer_class = ColumnSerializer





class TaskListApi(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComments.objects.all()
    serializer_class = CommentSerializer


class TaskDetailViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskDetailSerializer

    def update(self, request, pk=None):
        print(request.data)
        return super().update(request, pk=None)
