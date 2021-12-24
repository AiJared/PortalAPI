from rest_framework import serializers
from portal.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'course', 'period', 'reg_no')