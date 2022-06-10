from django.contrib import admin
from django.urls import path
from rest_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view(), name='studentapi'),
    # path('studentapi/', views.StudentCreate.as_view(), name='studentapi'),
    # path('studentapi/<int:pk>', views.StudentRetrieve.as_view(), name='studentapipk'),
    # path('studentapi/<int:pk>', views.StudentUpdate.as_view(), name='studentapipk'),
    # path('studentapi/<int:pk>', views.StudentDestroy.as_view(), name='studentapipk'),


    path('studentapi/', views.StudentListCreate.as_view(), name='studentapi'),
    # path('studentapi/<int:pk>', views.StudentRetrieveUpdate.as_view(), name='studentapipk'),
    # path('studentapi/<int:pk>', views.StudentRetrieveDestroy.as_view(), name='studentapipk'),

    path('studentapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view(), name='studentapipk'), 
]
