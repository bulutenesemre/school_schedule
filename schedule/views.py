from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Class, Subject, Teacher, Schedule
from .serializers import ClassSerializer, SubjectSerializer, TeacherSerializer, ScheduleSerializer
from datetime import datetime


class ClassCreateListAPIView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class SubjectCreateListAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TeacherCreateListAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ScheduleListAPIView(generics.ListCreateAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        class_name = self.request.query_params.get('class_name', None)
        for_today = self.request.query_params.get('for_today', 'false').lower() == 'true'

        queryset = Schedule.objects.all().select_related('class_name', 'subject', 'teacher')

        if class_name:
            queryset = queryset.filter(class_name__name=class_name)

        if for_today:
            today = datetime.today().strftime('%A')
            queryset = queryset.filter(day_of_week=today)

        return queryset


@api_view(['GET'])
def class_schedule_for_today(request):
    class_name = request.GET.get('class_name')
    today = datetime.today().strftime('%A')
    schedules = Schedule.objects.filter(class_name__name=class_name, day_of_week=today)
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)
