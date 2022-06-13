from .models import Student
from .serializers import StudentSerialiazer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerialiazer
	authentication_classes = [BasicAuthentication]
	# permission_classes = [IsAuthenticated]    #  Locally Declare
	# use authentication then write this class use authentication then write locally
	# permission_classes = [AllowAny]   # every user crud or any operations
	permission_classes = [IsAdminUser]