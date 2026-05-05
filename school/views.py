from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Enrollment, Attendance, Notification
from .serializers import (
    EnrollmentSerializer,
    AttendanceSerializer,
    NotificationSerializer
)

class StudentDashboardView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        student = request.user

        return Response({
            "courses": EnrollmentSerializer(
                Enrollment.objects.filter(student=student),
                many=True
            ).data,

            "attendance": AttendanceSerializer(
                Attendance.objects.filter(student=student),
                many=True
            ).data,

            "notifications": NotificationSerializer(
                Notification.objects.filter(student=student),
                many=True
            ).data,
        })

# Create your views here.
