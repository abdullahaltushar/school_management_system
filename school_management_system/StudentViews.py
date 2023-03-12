from django.shortcuts import render, redirect

from django.contrib import messages


from Account.models import Account
from schoolmanage.models import  Class, Subjects, Students, StudentResult
from django.contrib.auth.decorators import login_required

@login_required
def student_home(request):
    student_obj = Students.objects.get(admin=request.user.id)
    class_obj = Class.objects.get(id=student_obj.class_id.id)
    total_subjects = Subjects.objects.filter(class_id=class_obj).count()

    subject_name = []
    data_present = []
    data_absent = []
    subject_data = Subjects.objects.filter(class_id=student_obj.class_id)
    for subject in subject_data:
        subject_name.append(subject.subject_name)
        
    
    context={
        "total_subjects": total_subjects,
        "subject_name": subject_name,
        "data_present": data_present,
        "data_absent": data_absent
    }
    return render(request, "student_template/student_home_template.html", context)

@login_required
def student_profile(request):
    user = Account.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)

    context={
        "user": user,
        "student": student
    }
    return render(request, 'student_template/student_profile.html', context)

@login_required
def student_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('student_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            customuser = Account.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            student = Students.objects.get(admin=customuser.id)
            student.address = address
            student.save()
            
            messages.success(request, "Profile Updated Successfully")
            return redirect('student_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('student_profile')

@login_required
def student_view_result(request):
    student = Students.objects.get(admin=request.user.id)
    student_result = StudentResult.objects.filter(student_id=student.id)
    context = {
        "student_result": student_result,
    }
    return render(request, "student_template/student_view_result.html", context)





