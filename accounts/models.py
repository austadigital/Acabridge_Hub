from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

AFRICAN_COUNTRIES = [
    ("NG", "Nigeria"),
    ("GH", "Ghana"),
    ("KE", "Kenya"),
    ("ZA", "South Africa"),
    ("EG", "Egypt"),
    ("DZ", "Algeria"),
    ("MA", "Morocco"),
    ("TN", "Tunisia"),
    ("ET", "Ethiopia"),
    ("UG", "Uganda"),
    ("TZ", "Tanzania"),
    ("SN", "Senegal"),
    ("CI", "Côte d'Ivoire"),
    ("CM", "Cameroon"),
    ("ZW", "Zimbabwe"),
    ("SD", "Sudan"),
    ("LY", "Libya"),
    ("AO", "Angola"),
    ("MZ", "Mozambique"),
    ("MG", "Madagascar"),
    ("BF", "Burkina Faso"),
]    # you can expand this list


class Student(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    nationality = models.CharField(max_length=5, choices=AFRICAN_COUNTRIES, blank=True)
   
    bio = models.TextField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    