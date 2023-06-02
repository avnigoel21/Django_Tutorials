from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Receipe)

admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student' , 'subject' , 'marks']

admin.site.register(Subject)
admin.site.register(SubjectMarks , SubjectMarksAdmin)