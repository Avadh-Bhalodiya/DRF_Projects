from django.contrib import admin
from django.urls import path
from rest_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>', views.student_detail, name='student_detail'),
    path('stuinfo/', views.student_list, name='student_list'),
]
