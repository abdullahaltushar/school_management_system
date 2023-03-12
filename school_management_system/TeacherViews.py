from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Account.models import Account
from schoolmanage.models import Teacher, Class, Subjects, Students, SessionYearModel, StudentResult

@login_required
def Teacher_home(request):
    # Fetching All Students under Teacher
    id=Teacher.objects.get(admin=request.user.id) 
    subjects = Subjects.objects.filter(Teacher_id=id)
    class_id_list = []
    for subject in subjects:
        class1 = Class.objects.get(id=subject.class_id.id)
        class_id_list.append(class1.id)
    
    final_class = []
    # Removing Duplicate Class Id
    for class_id in class_id_list:
        if class_id not in final_class:
            final_class.append(class_id)
    
    students_count = Students.objects.filter(class_id__in=final_class).count()
    subject_count = subjects.count()

     #Fetch Attendance Data by Subjects
    subject_list = []
    for subject in subjects:
        subject_list.append(subject.subject_name)

    students_data = Students.objects.filter(class_id__in=final_class)
    student_list = []

    for student in students_data:
        student_list.append(student.admin.first_name+" "+ student.admin.last_name)

    context={
        "students_count": students_count,
        "subject_count": subject_count,
        "subject_list": subject_list,
        "student_list": student_list,
    }
    return render(request, "teacher_template/teacher_home_template.html", context)


@login_required
def teacher_profile(request):
    user = Account.objects.get(id=request.user.id)
    teacher = Teacher.objects.get(admin=user)

    context={
        "user": user,
        "teacher": teacher
    }
    return render(request, 'teacher_template/teacher_profile.html', context)


@login_required
def teacher_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('teacher_profile')
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

            teacher = Teacher.objects.get(admin=customuser.id)
            teacher.address = address
            teacher.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('teacher_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('teacher_profile')



@login_required
def teacher_add_result(request):
    id=Teacher.objects.get(admin=request.user.id) 
    subjects = Subjects.objects.filter(Teacher_id=id)
    session_years = SessionYearModel.objects.all()
    student=Students.objects.all()
    print(subjects)
    context = {
        "subjects": subjects,
        "session_years": session_years,
        "students":student,
    }
    return render(request, "teacher_template/add_result_template.html", context)


@login_required
def teacher_add_result_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('teacher_add_result')
    else:
        student_admin_id = request.POST.get('student')
        assignment_marks = request.POST.get('ass')
        exam_marks = request.POST.get('exam')
        subject_id = request.POST.get('subject')

        student_obj = Students.objects.get(admin=student_admin_id)
        subject_obj = Subjects.objects.get(id=subject_id)

        try:
            # Check if Students Result Already Exists or not
            check_exist = StudentResult.objects.filter(subject_id=subject_obj, student_id=student_obj).exists()
            if check_exist:
                result = StudentResult.objects.get(subject_id=subject_obj, student_id=student_obj)
                result.subject_assignment_marks = assignment_marks
                result.subject_exam_marks = exam_marks
                result.total_result= int(assignment_marks) + int(exam_marks)
                result.save()
                messages.success(request, "Result Updated Successfully!")
                return redirect('teacher_add_result')
            else:
                result = StudentResult(student_id=student_obj, subject_id=subject_obj, subject_exam_marks=exam_marks, subject_assignment_marks=assignment_marks)
                result.save()
                messages.success(request, "Result Added Successfully!")
                return redirect('teacher_add_result')
        except:
            messages.error(request, "Failed to Add Result!")
            return redirect('teacher_add_result')
