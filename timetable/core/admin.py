from django.contrib import admin

from .models import Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['no', 'division', 'name', 'professor', 'time_and_location']
    list_filter = ['is_FL', 'grade']
    search_fields = ['name', 'eng_name', 'professor', 'department']


admin.site.register(Subject, SubjectAdmin)
