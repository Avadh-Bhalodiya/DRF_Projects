from .models import Student
from .serializers import StudentSerialiazer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerialiazer
	authentication_classes = [SessionAuthentication]
	permission_classes = [IsAuthenticated]
	# permission_classes = [AllowAny]   # every user crud or any operations
	# permission_classes = [IsAdminUser]	#	staff status is active that user only crud opretions
	# permission_classes = [IsAuthenticatedOrReadOnly]
	# permission_classes = [DjangoModelPermissions] # By default only read permissions
	# permission_classes = [DjangoModelPermissionsOrAnonReadOnly]