# schedules/urls.py
from django.urls import path
from .views import ClassCreateListAPIView, SubjectCreateListAPIView, TeacherCreateListAPIView, ScheduleListAPIView

urlpatterns = [
    path('schedule/', ScheduleListAPIView.as_view(), name='schedule-list-create'),
    path('class/', ClassCreateListAPIView.as_view(), name='class-list-create'),
    path('subject/', SubjectCreateListAPIView.as_view(), name='subject-list-create'),
    path('teacher/', TeacherCreateListAPIView.as_view(), name='teacher-list-create'),
]
