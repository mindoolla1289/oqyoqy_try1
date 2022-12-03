from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Teacher, Student ,Lesson


class TeacherCreationForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ('username','email')

class TeacherChangeForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ('username','email')

class StudentCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ('username','email')

class StudentChangeForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ('username','email')