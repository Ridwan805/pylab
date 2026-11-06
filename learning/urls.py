from django.urls import path 
from . import views  

urlpatterns = [
    path("", views.home, name = 'home'), #path() definse the URL pattern, view.home refers to our home function, name="home" gives the URL a reusable name.

    path(
        "student/dashboard/",
        views.student_dashboard,
        name="student_dashboard"
    ),
    
    path(
        "manage/lessons/",
        views.manage_lessons,
        name="manage_lessons"
    ),
    
    path(
        "courses/<int:course_id>/",
        views.course_detail,
        name="course_detail"
    ),

    path(
    "courses/<int:course_id>/lessons/<int:lesson_id>/",
    views.lesson_detail,
    name="lesson_detail"
    ),

    path(
    "courses/<int:course_id>/lessons/<int:lesson_id>/complete/",
    views.complete_lesson,
    name="complete_lesson"
    ),
    
]


