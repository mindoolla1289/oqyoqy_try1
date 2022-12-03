from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Teacher, Student, Course,  Lesson


admin.site.register(Course)
admin.site.register(Lesson)

@admin.register(Teacher)
class CustomUserAdmin(UserAdmin):
    inlines = []

    model = Teacher


    list_display = ['username', 'phoneNumber','role']

    # Add user
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'username',
                    'phoneNumber',
                    'role',
                )
            }
        )
    )



@admin.register(Student)
class CustomUserAdmin(UserAdmin):
    inlines = []

    model = Student


    list_display = ['username', 'phoneNumber']

    # Add user
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'username',
                    'phoneNumber',
                )
            }
        )
    )


