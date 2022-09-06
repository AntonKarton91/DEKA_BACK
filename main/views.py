from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Tasks, TableColumns
from main.serializers import ColumnSerializer, TasksSerializer


class Index(TemplateView):
    template_name = './main/index.html'

# class TaskListApi(APIView):
#     def get(self, request):
#         lst = Tasks.objects.all()
#         lst1 = Tasks.objects.all().values()
#
#         return Response({"tasks": 'lst'})

class TaskListApi(ListAPIView):
    queryset = TableColumns.objects.all()
    serializer_class = ColumnSerializer

class SimpleListAPI(APIView):

    def get(self, request):
        if request.query_params.get('ikj'):
            print(request.query_params)
        return Response({'posts': "posts"})

    def post(self, request, *args, **kwargs):
        print(request.data)
        print(kwargs)
        # instance = Tasks.objects

        return Response({'posts': "posts"})