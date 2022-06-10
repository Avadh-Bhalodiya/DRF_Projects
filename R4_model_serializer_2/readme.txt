class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']
        extra_kwargs = {'name':{'read_only':True}}

- sortcut of Model_Serializer