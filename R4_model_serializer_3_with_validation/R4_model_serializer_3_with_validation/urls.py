from django.contrib import admin
from django.urls import path
from rest_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentApi.as_view(), name='student_api'),
]
