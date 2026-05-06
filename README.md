# 📘 Student Portal Backend API Documentation

This document describes the backend API structure for the Student Portal system built with Django + Django REST Framework + JWT Authentication.

---

# 🚀 Base URL

```
http://127.0.0.1:8000/api/
```

---

# 🔐 Authentication System

The system uses **JWT (JSON Web Token)** authentication.

### Header Format (for protected routes)

```
Authorization: Bearer <access_token>
```

---

# 📌 AUTH ENDPOINTS

## 1. Register Student

### Endpoint

```
POST /register/
```

### Request Body

```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

### Response

```json
{
  "message": "User created successfully"
}
```

---

## 2. Login Student

### Endpoint

```
POST /login/
```

### Request Body

```json
{
  "email": "string",
  "password": "string"
}
```

### Response

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

---

## 3. Refresh Token

### Endpoint

```
POST /refresh/
```

### Request Body

```json
{
  "refresh": "jwt_refresh_token"
}
```

### Response

```json
{
  "access": "new_access_token"
}
```

---

## 4. Logout Student

### Endpoint

```
POST /logout/
```

### Headers

```
Authorization: Bearer <access_token>
```

### Request Body

```json
{
  "refresh": "jwt_refresh_token"
}
```

### Response

```json
{
  "message": "Logged out successfully"
}
```

---

## 5. Student Profile

### Endpoint

```
GET /profile/
```

### Headers

```
Authorization: Bearer <access_token>
```

### Response

```json
{
  "id": 1,
  "username": "student1",
  "email": "student@email.com"
}
```

---

## 6. Student Dashboard

### Endpoint

```
GET /dashboard/
```

### Headers

```
Authorization: Bearer <access_token>
```

### Response

```json
{
  "courses": [],
  "attendance": [],
  "notifications": []
}
```

---

# 📊 DATABASE MODELS

## Student (Custom User Model)

* email (unique)
* username
* password

## Course

* title
* code

## Enrollment

* student (FK → Student)
* course (FK → Course)

## Attendance

* student (FK → Student)
* course (FK → Course)
* date
* present

## Notification

* student (FK → Student)
* message
* is_read

---

# 🔁 SYSTEM FLOW

```
Frontend (React/Lovable)
        ↓
Authentication (Login API)
        ↓
JWT Token Stored
        ↓
Protected API Calls
        ↓
Django Backend
        ↓
Database (SQLite/PostgreSQL)
```

---

# 🧠 BACKEND ARCHITECTURE

```
                ┌──────────────────────┐
                │   Frontend (React)   │
                │   or Lovable UI      │
                └─────────┬────────────┘
                          │ HTTP Requests
                          ↓
        ┌─────────────────────────────────┐
        │     Django REST API Layer       │
        │  - Auth (JWT)                  │
        │  - Dashboard API              │
        │  - Profile API                │
        │  - Attendance API             │
        └─────────┬──────────────────────┘
                  │
                  ↓
        ┌───────────────────────────────┐
        │        Django Models          │
        │  Student, Course, Attendance  │
        │  Enrollment, Notification     │
        └─────────┬─────────────────────┘
                  │
                  ↓
        ┌───────────────────────────────┐
        │        Database               │
        │   SQLite / PostgreSQL        │
        └───────────────────────────────┘
```

---

# 🔐 SECURITY RULES

* All sensitive endpoints require JWT token
* Tokens must be passed via Authorization header
* Refresh tokens are used to generate new access tokens
* Logout blacklists refresh token

---

# 🧪 TESTING CHECKLIST

* [x] Register works
* [x] Login returns tokens
* [x] Profile requires authentication
* [x] Dashboard returns structured data
* [x] Logout invalidates token

---

# 🚀 FRONTEND INTEGRATION RULES

* Base URL: `http://127.0.0.1:8000/api/`
* Store tokens in localStorage
* Attach access token to all protected requests
* Refresh token when access expires

---

# 📌 NOTES FOR FRONTEND ENGINEER

* Use Bearer token authentication
* Handle 401 errors by refreshing token
* Redirect to login if refresh fails

---

# ✅ PROJECT STATUS

✔ Authentication System: COMPLETE
✔ API Structure: COMPLETE
✔ Frontend Ready: YES
✔ Production Ready: YES (after deployment)

# 🧪 API Testing Guide

## Base URL

http://127.0.0.1:8000/api/

---

## 🔐 Authentication Flow

1. Login → get access + refresh token
2. Use access token for protected routes
3. Refresh token when expired
4. Logout to invalidate session

---

## 📌 Endpoints Tested

### ✅ Login

POST /api/login/

### ✅ Profile

GET /api/profile/

### ✅ Tracks (Dropdown)

GET /api/tracks/

### ✅ Update Profile

PUT /api/profile/update/

### ✅ Application Status

GET /api/application-status/

### ✅ Dashboard

GET /api/dashboard/

### ✅ Logout

POST /api/logout/

---

## 🔐 Authorization Header

All protected routes require:

Authorization: Bearer <access_token>

---

## 🧪 Testing Tools

* Thunder Client (VS Code)
* Postman (optional)

---

## ⚠️ Common Errors

| Error            | Cause                 |
| ---------------- | --------------------- |
| 401 Unauthorized | Missing/expired token |
| 404 Not Found    | Wrong URL             |
| Invalid Token    | Wrong refresh token   |

---


---

# 🚀 How to Run the Project

```bash
git clone <https://github.com/austadigital/Acabridge_Hub.git>
cd acabridge_student_portal

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

# 👨‍💻 MAINTAINER

Backend Developer: Django REST API Team
