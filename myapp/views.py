from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Admission, StudentDocument, UserProfile

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        full_name = request.POST['full_name']
        mobile_number = request.POST['mobile_number']
        birthdate = request.POST['birthdate']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(
            user=user,
            full_name=full_name,
            mobile_number=mobile_number,
            birthdate=birthdate,
            email=email
        )

        messages.success(request, "✅ Registered successfully. Please login.")
        return redirect('login')

    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "✅ Login successful!")
            return redirect('admission_manual')
        else:
            messages.error(request, '❌ Invalid credentials. Please try again.')
            return redirect('login')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "✅ Logged out successfully.")
    return redirect('login')


@login_required
def admission_manual(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']
        message = request.POST['message']

        admission = Admission.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            course=course,
            message=message
        )

        messages.success(request, "✅ Admission form submitted successfully.")
        return redirect('student_info', admission_id=admission.id)

    return render(request, 'admission_form.html')


@login_required
def student_info(request, admission_id):
    admission = get_object_or_404(Admission, pk=admission_id)
    if request.method == 'POST':
        StudentDocument.objects.create(
            admission=admission,
            tenth_marksheet=request.FILES['tenth_marksheet'],
            leaving_certificate=request.FILES['leaving_certificate'],
            adhar_card=request.FILES['adhar_card']
        )
        messages.success(request, "✅ Documents uploaded successfully.")
        return redirect('success')

    return render(request, 'student_info.html', {'admission_id': admission_id})


@login_required
def success(request):
    return render(request, 'success.html')
