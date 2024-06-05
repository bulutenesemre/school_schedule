from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    # Assuming a student belongs to only one class
    class_name = models.ForeignKey('Class', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    # Assuming each class has a fixed number of students
    student_count = models.IntegerField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    class_name = models.ForeignKey('Class', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, db_index=True)  # Assuming Monday, Tuesday, etc.
    hour = models.IntegerField()  # Assuming hour of the day (e.g., 9 for 9 AM)

    class Meta:
        ordering = ['day_of_week', 'hour']
        indexes = [
            models.Index(fields=['day_of_week']),
            models.Index(fields=['class_name', 'day_of_week']),
        ]

    def __str__(self):
        return f"{self.class_name} - {self.subject} - {self.day_of_week} at {self.hour}:00"

