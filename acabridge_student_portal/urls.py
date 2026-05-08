"""
URL configuration for acabridge_student_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import RegisterView, ProfileView, EmailLoginView, LogoutView, UpdateProfileView  
from rest_framework_simplejwt.views import TokenRefreshView
from school.views import StudentDashboardView, TrackListView, ApplicationStatusView
from django.http import HttpResponse

def home(request):
    return HttpResponse("AcaBridge Backend is Live 🚀")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view()),
    path('api/login/', EmailLoginView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/profile/', ProfileView.as_view()),
    path('api/logout/', LogoutView.as_view()), 
    path('api/tracks/', TrackListView.as_view()),
    path('api/profile/update/', UpdateProfileView.as_view()),
    path('api/application-status/', ApplicationStatusView.as_view()),

    # DASHBOARD
    path('api/dashboard/', StudentDashboardView.as_view()),
]
