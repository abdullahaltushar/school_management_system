from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are now logged in")
            user_type = user.profile_type
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == 'superuser':
                return redirect('admin_home')
            elif user_type == 'teacher':
                # return HttpResponse("Staff Login")
                return redirect('teacher_home')
                
            elif user_type == 'student':
                # return HttpResponse("Student Login")
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
    return render(request,'accounts/login.html')

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,"You are logged out")
    return redirect('login')