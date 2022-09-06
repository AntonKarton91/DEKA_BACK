from django.contrib import admin
from django.urls import path, include

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('api/v1/tasklist/', TaskListApi.as_view()),
    path('api/v1/tasklist1/', SimpleListAPI.as_view()),
]
