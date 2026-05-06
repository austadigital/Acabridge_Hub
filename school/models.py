from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Attendance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)


class Notification(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

class Track(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Application(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    submitted_at = models.DateTimeField(auto_now_add=True)