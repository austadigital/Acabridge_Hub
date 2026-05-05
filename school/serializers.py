from rest_framework import serializers
from .models import Course, Enrollment, Attendance, Notification

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = ['course']


class AttendanceSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Attendance
        fields = ['course', 'date', 'present']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'