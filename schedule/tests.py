# schedules/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Class, Subject, Teacher, Schedule
from freezegun import freeze_time
import datetime


class ScheduleAPITests(APITestCase):

    def setUp(self):
        self.class_5A = Class.objects.create(name="5A", student_count=23)
        self.math_subject = Subject.objects.create(name="Math")
        self.teacher = Teacher.objects.create(name="Enes")
        self.schedule = Schedule.objects.create(
            class_name=self.class_5A,
            subject=self.math_subject,
            teacher=self.teacher,
            day_of_week="Monday",
            hour=9
        )

    def test_create_class(self):
        url = reverse('class-list-create')
        data = {'name': '6A', 'student_count': 25}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Class.objects.count(), 2)
        created_class = Class.objects.get(name='6A')
        self.assertEqual(created_class.student_count, 25)

    def test_create_subject(self):
        url = reverse('subject-list-create')
        data = {'name': 'Science'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subject.objects.count(), 2)
        created_subject = Subject.objects.get(name='Science')
        self.assertEqual(created_subject.name, 'Science')

    def test_create_teacher(self):
        url = reverse('teacher-list-create')
        data = {'name': 'Emre'}
        response = self.client.post(url, data, format='Emre')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Teacher.objects.count(), 2)
        created_teacher = Teacher.objects.get(name='Emre')
        self.assertEqual(created_teacher.name, 'Emre')

    def test_create_schedule(self):
        url = reverse('schedule-list-create')
        data = {
            'class_name': self.class_5A.id,
            'subject': self.math_subject.id,
            'teacher': self.teacher.id,
            'day_of_week': 'Tuesday',
            'hour': 10
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Schedule.objects.count(), 2)
        created_schedule = Schedule.objects.get(day_of_week='Tuesday')
        self.assertEqual(created_schedule.hour, 10)

    @freeze_time("2024-06-10")
    def test_get_all_schedules(self):
        url = reverse('schedule-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['day_of_week'], 'Monday')

    @freeze_time("2024-06-10")
    def test_get_class_schedule_for_today(self):
        url = reverse('schedule-list-create')
        response = self.client.get(url, {'for_today': 'true', 'class_name': '5A'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['day_of_week'], 'Monday')
