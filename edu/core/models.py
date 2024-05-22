
# Create your models here.
# core/models.py

from django.contrib.auth.models import AbstractUser,Group, Permission

from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)
    moderators = models.ManyToManyField(User, related_name='moderated_courses', blank=True)

    def __str__(self):
        return f'{self.title}'

class Module(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    module = models.ForeignKey(Module, related_name='assignments', on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='assignments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='assignments/')

class Grade(models.Model):
    grade = models.IntegerField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.student.username}'s grade for {self.assignment.title}"

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.title}'