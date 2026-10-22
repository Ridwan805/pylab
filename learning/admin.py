from django.contrib import admin
from .models import Course, Lesson 
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",'id',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "course", "order")
    list_display_links = ("title",)
    list_filter = ("course",)
    search_fields = ("title", "content")
    ordering = ("course", "order")