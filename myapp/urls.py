from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('admission_manual/', views.admission_manual, name='admission_manual'),
    path('student-info/<int:admission_id>/', views.student_info, name='student_info'),
    path('success/', views.success, name='success'),
]
