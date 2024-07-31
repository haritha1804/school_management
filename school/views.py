from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *


class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
class class1ViewSet(viewsets.ModelViewSet):
    queryset = Class1.objects.all()
    serializer_class = class1Serializer
class studentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = studentSerializer
class teacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = teacherSerializer
class subjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = subjectSerializer
class enrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = enrollmentSerializer
class examViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = examSerializer
class resultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = resultSerializer
class attendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = attendanceSerializer
class roomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = roomSerializer
class timetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = timetableSerializer
class eventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = eventSerializer