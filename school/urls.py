from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'user', userViewSet)
router.register(r'class', class1ViewSet)
router.register(r'student', studentViewSet)
router.register(r'teacher', teacherViewSet)
router.register(r'subject', subjectViewSet)
router.register(r'enrollment', enrollmentViewSet)
router.register(r'exam', examViewSet)
router.register(r'result', resultViewSet)
router.register(r'attendances', attendanceViewSet)
router.register(r'room', roomViewSet)
router.register(r'timetable', timetableViewSet)
router.register(r'event', eventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
