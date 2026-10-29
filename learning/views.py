from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.urls import reverse
from django.utils.html import escape
from django.middleware.csrf import get_token

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from .models import Course, Lesson

# Create your views here.
def home(request):
    courses = Course.objects.all().order_by("-created_at")[:3]

    return render(request, "learning/home.html", {
        "courses": courses
    })

@login_required
def student_dashboard(request):
    courses = Course.objects.all().order_by("id")

    return render(request, "learning/student_dashboard.html", {
        "courses": courses
    })


@login_required
@permission_required("learning.view_lesson", raise_exception=True)
def manage_lessons(request):
    lessons = Lesson.objects.select_related("course").order_by(
        "course__title", "order"
    )

    return render(request, "learning/manage_lessons.html", {
        "lessons": lessons
    })

