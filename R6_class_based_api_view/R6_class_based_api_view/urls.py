from django.contrib import admin
from django.urls import path
from rest_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentAPI.as_view(), name='studentapi'),
    path('studentapi/<int:pk>', views.StudentAPI.as_view(), name='studentapipk'),
]
