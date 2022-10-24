from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

router = SimpleRouter()
router.register(r'marks', MarkViewSet)
router.register(r'users', UserViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'columnlist', ColumnListApi)
router.register(r'task', TaskListApi)
router.register(r'taskdetail', TaskDetailViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('api/v1/addcolumn/', AddColumnAPIView.as_view()),
    path('api/v1/list/', ColumnANDListApi.as_view()),
    path('api/v1/addtask/', AddTaskAPI.as_view()),
    path('api/v1/register/', CreateUser.as_view()),
    path('api/v1/dnd/', DNDView.as_view()),
    path('api/v1/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
