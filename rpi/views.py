from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from portal.models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer