from django.urls import path
from .views import *

urlpatterns = [
    # Test
    path('users/all', AllUsersView.as_view()),
    path('courses/all', AllCoursesView.as_view()),
    path('course/students/<int:pk>', CourseStudents.as_view()),

    # TeachersViews
    # Course
    path('course/<int:pk>', CourseView.as_view()),
    path('course/new', CourseCreateView.as_view()),
    path('course/all', CourseListView.as_view()),
    # Lessons
    path('lesson/<int:pk>', LessonView.as_view()),
    path('lesson/new', LessonCreateView.as_view()),
    path('lesson/all/<int:pk>', CourseLessonsListView.as_view()),
    # Teacher's students
    path('tstudent/all', TeachersStudetsList.as_view()),
    path('tstudent/addstudent/<int:pk>', AddStudentToCourse.as_view({'get': 'retrieve', 'patch': 'update'})),


    path('mycourses/', StudensCourseListView.as_view()),
    path('course/lessons/<int:pk>', StudensCourseListView.as_view()),
]