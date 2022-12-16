from rest_framework import serializers

from .models import *




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'is_teacher','is_student']

class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'is_teacher','is_student','created_by']

class StudetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'email', 'first_name', 'last_name', 'is_teacher', 'is_student', 'created_by']


class AddStudetnToCourse(serializers.ModelSerializer):
    class Meta:
        model = Course


class CourseSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='user.username')
    teachers = serializers.ReadOnlyField(source='user.username')
    students = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Course
        fields = '__all__'

    def update(self, instance, validated_data):
        items = self.initial_data['students']
        i = instance
        for item in items:
            student = CustomUser.objects.get(id=item)
            i.students.add(student)
        i.save()
        return instance

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'



class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'



class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'email', 'first_name', 'last_name', 'is_teacher','is_student','created_by']


class TestCourseSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='user.username')
    teachers = serializers.ReadOnlyField(source='user.username')
    students = StudetSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'
