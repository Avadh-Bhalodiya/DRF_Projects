from unittest.result import STDOUT_LINE
from .models import Student
from .serializers import StudentSerialiazer
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiazer