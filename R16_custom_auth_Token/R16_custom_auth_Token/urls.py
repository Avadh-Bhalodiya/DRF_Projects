from django.contrib import admin
from django.urls import path, include
from rest_app import views
from rest_framework.routers import DefaultRouter
from rest_app.auth import CustomAuthToken

# Create Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename='studentapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    #   login option enable 
    path('gettoken/', CustomAuthToken.as_view()),
]