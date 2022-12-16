from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets, response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .permissions import *




# Teacher's viws
# Teacher course view

# Создать курс
class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_class = permissions.IsAuthenticated

# Просмотр, обновить, удалить курс
class CourseView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_class = permissions.IsAuthenticated
    permission_classes_by_action = {'get': [permissions.IsAuthenticated],
                                    'update': [permissions.IsAuthenticated],
                                    'destroy': [permissions.IsAuthenticated]}

# Список курсов Учителья
class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_class = permissions.IsAuthenticated

    def get_queryset(self):
        return Course.objects.filter(creator__exact=self.request.user)

# Teacher Lessons views
# Lesson's views

# Создать урок
class LessonCreateView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer
    permission_class = permissions.IsAuthenticated

# Просмотр, обновить, удалить урок
class LessonView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_class = permissions.IsAuthenticated
    permission_classes_by_action = {'get': [permissions.IsAuthenticated],
                                    'update': [IsCreator],
                                    'destroy': [IsCreator]}

# Список уроков курса
class CourseLessonsListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_class = permissions.IsAuthenticated

    def get_queryset(self):
        return Lesson.objects.filter(course_id__exact=self.kwargs.get('pk'))






class TeachersStudetsList(generics.ListAPIView):
    serializer_class = StudetSerializer
    permission_classees = (permissions.IsAuthenticated, IsTeacher)

    def get_queryset(self):
        return CustomUser.objects.filter(created_by__exact=self.request.user.username)


class AddStudentToCourse(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_class = permissions.IsAuthenticated
    # permission_classes_by_action = {'get': [permissions.IsAuthenticated],
    #                                 'update': [IsCreator],
    #                                 'destroy': [IsCreator]}




class addStudent(APIView):
    permission_class = permissions.IsAuthenticated
    def post(self, obj ,request, pk):
        try:
            Kurs = Course.objects.get(id=pk)
        except:
            return response.Response(status=404)
        Kurs.students.add()


#
#
#
# # Student's views
class StudensCourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated,IsStudent)
    def get_queryset(self):
        return Course.objects.all().filter(students__exact=self.request.user)

class StudentCourseLessonsListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_class = permissions.IsAuthenticated

    def get_queryset(self):
        return Lesson.objects.filter(course_id__exact=self.kwargs.get('pk'))



# #Testing views

class AllUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AllUserSerializer
    permission_class = permissions.IsAuthenticated

class AllCoursesView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseStudents(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = TestCourseSerializer
