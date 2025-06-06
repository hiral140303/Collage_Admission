from django.contrib import admin
from .models import Admission,StudentDocument,UserProfile


# Register your models here.
admin.site.register(Admission)
admin.site.register(StudentDocument)
admin.site.register(UserProfile)