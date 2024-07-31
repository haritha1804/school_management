# from django.utils import timezone
from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.user_name} {self.user_email}"

class Class1(models.Model):
    class_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.class_name

class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    admission_date = models.DateField()
    class1 = models.ForeignKey(Class1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.user_name} {self.class1.class_name}"

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    class1 = models.ForeignKey(Class1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_name} {self.class1.class_name}"

class Teacher(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacherid')
    class1 = models.ForeignKey(Class1, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teacheremail')

    def __str__(self):
        return f"{self.teacher.user_name} {self.class1.class_name} {self.subject.subject_name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class1 = models.ForeignKey(Class1, on_delete=models.CASCADE)
    # date = models.DateField(default=timezone.now)
    def __str__(self):
        return f"{self.student.student.user_name} {self.class1.class_name}"

class Exam(models.Model):
    class1 = models.ForeignKey(Class1, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return f"{self.class1.class_name}"

class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    mark = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.exam.exam_name} {self.enrollment.class1.class_name} {self.enrollment.student.student.user_name}"

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student.user_name}"

class Room(models.Model):
    room_number = models.CharField(max_length=15)

    def __str__(self):
        return self.room_number

class Timetable(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.teacher.user_name} {self.subject.subject_name} {self.room.room_number}"

class Event(models.Model):
    event_user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room.room_number}"
