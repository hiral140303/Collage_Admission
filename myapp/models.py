from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    birthdate = models.DateField()
    email = models.EmailField()

class Admission(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    message = models.TextField()

class StudentDocument(models.Model):
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE)
    tenth_marksheet = models.FileField(upload_to='documents/')
    leaving_certificate = models.FileField(upload_to='documents/')
    adhar_card = models.FileField(upload_to='documents/')
