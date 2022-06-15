from .models import Student
from .serializers import StudentSerialiazer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerialiazer
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]