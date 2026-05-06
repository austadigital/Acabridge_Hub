from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment, Attendance, Notification, Track, Application   
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
class TrackListView(APIView):
    def get(self, request):
        tracks = Track.objects.all()
        data = [{"id": t.id, "name": t.name} for t in tracks]
        return Response(data)
    
class ApplicationStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        app = Application.objects.filter(student=request.user).first()

        if not app:
            return Response({"status": "not_applied"})

        return Response({
            "status": app.status,
            "submitted_at": app.submitted_at
        })