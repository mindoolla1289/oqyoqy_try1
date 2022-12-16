from rest_framework import permissions
from rest_framework.permissions import BasePermission



class IsCreator(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.creator.user == request.user


class IsTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_teacher==True


class IsStudent(BasePermission):

    def has_object_permission(self, request, view, obj):
        o=obj
        return obj.students.user == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user