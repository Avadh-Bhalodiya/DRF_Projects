from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # Validators
    def start_with_a(value):
        if value[0].lower() != 'a':
            raise serializers.ValidationError('Name start must with A')
    
    name = serializers.CharField(validators = [start_with_a])

    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    #   field validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    #   object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'amit' and ct.lower() != 'bhuj':
            raise serializers.ValidationError('City must be rajkot')
        return data 
    