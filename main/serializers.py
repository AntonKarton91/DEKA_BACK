from django.db.migrations import serializer
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from main.models import Tasks, TableColumns


class TasksSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields =['task_name']

class ColumnSerializer(ModelSerializer):
    tasks = SerializerMethodField('getField')

    def getField(self, obj):
        a = getattr(obj, 'id')
        queryset = Tasks.objects.all().values()
        b = [i for i in queryset if i.get( 'column_id') == a]
        print(b)
        print(141343243)
        return b

    class Meta:
        model = TableColumns
        fields = ['id', 'column_name', 'column_type', 'tasks']