from rest_framework import serializers
from .models import *

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class class1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Class1
        fields = '__all__'
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
class enrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
class examSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
class resultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
class timetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'
class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'