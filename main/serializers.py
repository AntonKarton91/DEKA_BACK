# from django.contrib.postgres.fields import ArrayField
from django.db.migrations import serializer
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, ListField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from main.models import *


class UserSerializer(ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'ava', 'first_name', 'last_name', 'initials', 'password', 'token', 'id']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class CommentSerializer(ModelSerializer):
    class Meta:
        model = TaskComments
        fields = ['task', 'creater', 'createDate', 'body']


class MarkSerializer(ModelSerializer):
    class Meta:
        model = Marks
        fields = ['title', 'color', 'id']


class TasksSerializer(ModelSerializer):
    participants = PrimaryKeyRelatedField(many=True, read_only=True, allow_empty=True, required=False)
    marks = PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Tasks
        fields = ['id', 'name', 'participants', 'marks', 'date', "column"]


class TaskDetailSerializer(ModelSerializer):
    participants = PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all())
    marks = PrimaryKeyRelatedField(queryset=Marks.objects.all(), many=True)
    comments = CommentSerializer(many=True, source='task_comment', read_only=True)
    creater = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tasks
        fields = ['id', 'taskPosition', 'name', 'participants', 'marks',
                  'date', "column", "taskDescription", "comments", "creater"]


class ColumnSerializer(ModelSerializer):
    class Meta:
        model = TableColumns
        fields = ['id', 'order', 'columnName', 'columnType', 'tasks']




