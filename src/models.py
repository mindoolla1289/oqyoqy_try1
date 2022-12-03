from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class CustomUser(AbstractUser):
    """ Наш кастом юзер """
    id = models.BigAutoField(primary_key=True)
    phoneNumber = models.CharField("Номер телефона",max_length=14)

class Teacher(CustomUser):
    """  Учитель и админ  """
    ROLES = (
        ('T', 'Учитель'),
        ('A', 'Админ'),
    )
    role = models.CharField('Роль', max_length=1, choices=ROLES,default = '')
    courses = models.ManyToManyField('Course', through='Teacher_Course_junctioon',blank=True, null=True, related_name='курсы')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("Учитель")
        verbose_name_plural = _("Учитель")


class Course(models.Model):
    """ Курс """
    id = models.BigAutoField(primary_key=True)
    title = models.CharField("НазваниеКурса",max_length=100)
    description = models.TextField("ОписаниеКурса",blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Курс")
        verbose_name_plural = _("Курс")

class  Teacher_Course_junctioon(models.Model):
    id = models.BigAutoField(primary_key=True)
    teacher_id  = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    cours_id = models.ForeignKey(to=Course, on_delete=models.CASCADE)

class Lesson(models.Model):
    """ Урок """
    id = models.BigAutoField(primary_key=True)
    number = models.PositiveIntegerField(max_length=100,blank=True, null=True)
    title = models.CharField("Название Урока",max_length=100,blank=True, null=True)
    discription = models.TextField("Описание Урока",blank=True, null=True)
    content  = RichTextField(blank=True, null=True)
    course_id = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Урок")
        verbose_name_plural = _("Урок")

class Сourse_student_junction(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    cours_id = models.ForeignKey(to=Course, on_delete=models.CASCADE)

class Student(CustomUser):
    """ Студент """
    teacher_id = models.ManyToManyField(to=Teacher,through='Teacher_Students_junctioon',)
    course_id = models.ManyToManyField(to=Course, through=Сourse_student_junction)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("студент")
        verbose_name_plural = _("студент")


class  Teacher_Students_junctioon(models.Model):
    id = models.BigAutoField(primary_key=True)
    teacher_id  = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    Student_id = models.ForeignKey(to=Student, on_delete=models.CASCADE)