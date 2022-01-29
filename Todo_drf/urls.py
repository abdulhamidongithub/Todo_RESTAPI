from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from todoapp.views import TodoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Todo-Rest API",
      default_version='v1',
      description="Todo loyihasi uchun yaratilgan Rest API'lar to'plami",
      contact=openapi.Contact("Abdulhamid Egamberdiyev, <1997abdulhamid@gmail.com>"),
   ),
   public=True,
)


router = DefaultRouter()
router.register('todo', TodoViewSet, basename="todo")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('token/', obtain_auth_token),
    path('get-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    #Open API Documentation
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0)),
    # path('redoc/', schema_view.with_ui("redoc", cache_timeout=0)),
]
