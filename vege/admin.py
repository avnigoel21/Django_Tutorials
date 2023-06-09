from django.contrib import admin

from django.db.models import Sum

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



class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student' , 'student_rank'  ,  'date_of_report_card_generation']

    # def total_marks(self , obj):
    #     subject_marks = SubjectMarks.object.filter(student = obj.student)
    #     marks = (subject_marks.aggregate(marks = Sum('marks')))
    #     return marks['marks']


admin.site.register(ReportCard , ReportCardAdmin)