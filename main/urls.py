from django.urls import path, include

from .views import *

urlpatterns = [
    path('', Index.as_view()),
    path('api/v1/tasklist/', TaskListApi.as_view()),
]