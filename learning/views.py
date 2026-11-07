from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.utils.html import escape
from django.middleware.csrf import get_token

from django.contrib.auth.decorators import login_required, permission_required
from .models import Course, Lesson, LessonProgress

from django.shortcuts import redirect
from django.views.decorators.http import require_POST


from django.shortcuts import get_object_or_404

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

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    lessons = list(
        course.lessons.all().order_by("order", "id")
    )

    completed_ids = set(
        LessonProgress.objects.filter(
            student=request.user,
            lesson__course=course
        ).values_list("lesson_id", flat=True)
    )

    total_lessons = len(lessons)
    completed_count = len(completed_ids)

    progress_percentage = (
        round((completed_count / total_lessons) * 100)
        if total_lessons > 0
        else 0
    )

    for lesson in lessons:
        lesson.is_completed = lesson.id in completed_ids

    return render(request, "learning/course_detail.html", {
        "course": course,
        "lessons": lessons,
        "total_lessons": total_lessons,
        "completed_count": completed_count,
        "progress_percentage": progress_percentage,
    })


@login_required
def lesson_detail(request, course_id, lesson_id):
    lesson = get_object_or_404(
        Lesson.objects.select_related("course"),
        id=lesson_id,
        course_id=course_id
    )

    is_completed = LessonProgress.objects.filter(
        student=request.user,
        lesson=lesson
    ).exists()

    return render(
        request,
        "learning/lesson_detail.html",
        {
            "lesson": lesson,
            "course": lesson.course,
            "is_completed": is_completed
        }
    )


@login_required
@require_POST
def complete_lesson(request, course_id, lesson_id):
    lesson = get_object_or_404(
        Lesson,
        id=lesson_id,
        course_id=course_id
    )

    LessonProgress.objects.get_or_create(
        student=request.user,
        lesson=lesson
    )

    return redirect(
        "lesson_detail",
        course_id=course_id,
        lesson_id=lesson_id
    )