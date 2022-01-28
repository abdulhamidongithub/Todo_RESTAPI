from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from todoapp.views import TodoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('todo', TodoViewSet, basename="todo")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('token/', obtain_auth_token),
    path('get-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
]
