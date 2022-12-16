from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings

from ckeditor.fields import RichTextField



class CustomUser(AbstractUser):

    is_teacher = models.BooleanField()
    is_student = models.BooleanField()

    ROLE_TYPES = [
        ('1', 'Учитель'),
        ('2', 'Админ'),
        ('3', 'Студент'),
    ]
    role = models.CharField('Роль', choices=ROLE_TYPES, default='1', max_length=1)

    phoneNumber = models.CharField("Номер телефона", max_length=14)
    created_by = models.CharField("СоздательСтудента",max_length=100,blank=True, null=True)

    REQUIRED_FIELDS = ['first_name','last_name','phoneNumber','is_teacher','is_student','created_by','role']


    def __str__(self):
        return '{}, {}, role: {}'.format(self.username, self.get_role_display(), self.ROLE_TYPES)

    def __str__(self):
        return self.username




class Course(models.Model):
    """ Курс """
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='CourseCreator')
    title = models.CharField("НазваниеКурса",max_length=100)
    description = models.TextField("ОписаниеКурса",blank=True, null=True)
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='CourseTeachers')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='CourseStudents', null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Курс")
        verbose_name_plural = _("Курс")



class Lesson(models.Model):
    """ Урок """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='Курс')
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    title = models.CharField("Название Урока",max_length=100,blank=True, null=True)
    discription = models.TextField("Описание Урока",blank=True, null=True)
    content  = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Урок")
        verbose_name_plural = _("Урок")

class CompletedLessons(models.Model):
    lesson = models. ForeignKey(Lesson, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)