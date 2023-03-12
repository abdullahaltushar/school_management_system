from django.contrib import admin

# Register your models here.
from .models import Students,StudentResult,SessionYearModel,Subjects,Teacher,Class

admin.site.register(Students)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(StudentResult)
admin.site.register(Subjects)
admin.site.register(SessionYearModel)