from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Enrollment
from .serializers import (
    CourseSerializer,
    StudentSerializer
)


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=["get"])
    def students(self, request, pk=None):

        enrollments = Enrollment.objects.filter(
            course_id=pk
        )

        students = [
            enrollment.student
            for enrollment in enrollments
        ]

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)