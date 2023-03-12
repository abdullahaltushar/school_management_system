from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages#To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from Account.models import Account
from schoolmanage.models import Students, Class, Subjects, Teacher,SessionYearModel


@login_required
def admin_home(request):
   
    all_student_count =Students.objects.all().count()
    subject_count = Subjects.objects.all().count()
    class_count = Class.objects.all().count()
    Teacher_count = Teacher.objects.all().count()
    # return HttpResponse('admin')

    # Total Subjects and students in Each Course
    class_all = Class.objects.all()
    class_name_list = []
    subject_count_list = []
    student_count_list_in_class = []

    for class1 in class_all:
        subjects = Subjects.objects.filter(class_id=class1.id).count()
        students = Students.objects.filter(class_id=class1.id).count()
        class_name_list.append(class1.class_name)
        subject_count_list.append(subjects)
        student_count_list_in_class.append(students)
    
    subject_all = Subjects.objects.all()
    subject_list = []
    student_count_list_in_subject = []
    for subject in subject_all:
        class1 = Class.objects.get(id=subject.class_id.id)
        student_count = Students.objects.filter(class_id=class1.id).count()
        subject_list.append(subject.subject_name)
        student_count_list_in_subject.append(student_count)
     # For Students
    student_name_list=[]

    students = Students.objects.all()
    for student in students:
        student_name_list.append(student.admin.first_name)


    context={
        "all_student_count": all_student_count,
        "subject_count": subject_count,
        "course_count": class_count,
        "teacher_count": Teacher_count,
        "class_name_list": class_name_list,
        "subject_count_list": subject_count_list,
        "student_count_list_in_class": student_count_list_in_class,
        "subject_list": subject_list,
        "student_count_list_in_subject": student_count_list_in_subject,
        "student_name_list": student_name_list,
    }
    return render(request, "hod_template/home_content.html", context)

@login_required
def add_teacher(request):
    return render(request, "hod_template/add_teacher_template.html")

@login_required
def add_teacher_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_teacher')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone=request.POST.get('phone')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        father_name=request.POST.get('father_name')
        mother_name=request.POST.get('mother_name')
        myfile=request.FILES['myfile']

        try:
            user = Account.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            data=Account.objects.get(username=username)
            data.phone_number=phone
            data.dob=dob
            data.gender=gender
            data.father_name=father_name
            data.mother_name=mother_name
            data.image=myfile
            data.profile_type='teacher'
            data.save()
            teacher=Teacher.objects.create(admin=user)
            teacher.address=address
            teacher.save()
           
           
            messages.success(request, "Teacher Added Successfully!")
            return redirect('add_teacher')
        except:
            messages.error(request, "Failed to Add teacher!")
            return redirect('add_teacher')


@login_required
def manage_teacher(request):
    teacher= Teacher.objects.all()
    context = {
        "staffs": teacher
    }
    return render(request, "hod_template/manage_teacher_template.html", context)

@login_required
def edit_teacher(request, teacher_id):
    teacher = Teacher.objects.get(admin=teacher_id)

    context = {
        "teacher": teacher,
        "id": teacher_id
    }
    return render(request, "hod_template/edit_teacher_template.html", context)

@login_required
def edit_teacher_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        teacher_id = request.POST.get('teacher_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        father_name=request.POST.get('father_name')
        mother_name=request.POST.get('mother_name')
        phone_number=request.POST.get('phone')

        try:
            # INSERTING into Customuser Model
            user = Account.objects.get(id=teacher_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.father_name=father_name
            user.mother_name=mother_name
            user.phone_number=phone_number
            user.save()
            
            # INSERTING into Teacher Model
            teacher_model = Teacher.objects.get(admin=teacher_id)
            teacher_model.address = address
            teacher_model.save()

            messages.success(request, "teacher Updated Successfully.")
            return redirect('/edit_teacher/'+teacher_id)

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('/edit_teacher/'+teacher_id)


@login_required
def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(admin=teacher_id)
    try:
        teacher.delete()
        messages.success(request, "teacher Deleted Successfully.")
        return redirect('manage_teacher')
    except:
        messages.error(request, "Failed to Delete teacher.")
        return redirect('manage_teacher')



@login_required
def add_class(request):
    return render(request, "hod_template/add_class_template.html")

@login_required
def add_class_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_class')
    else:
        class1 = request.POST.get('class')
        try:
            class_model = Class(class_name=class1)
            class_model.save()
            messages.success(request, "Class Added Successfully!")
            return redirect('add_class')
        except:
            messages.error(request, "Failed to Add Class!")
            return redirect('add_class')

@login_required
def manage_class(request):
    classes = Class.objects.all()
    context = {
        "classs": classes
    }
    return render(request, 'hod_template/manage_class_template.html', context)

@login_required
def edit_class(request, class_id):
    class1 = Class.objects.get(id=class_id)
    context = {
        "class": class1,
        "id": class_id
    }
    return render(request, 'hod_template/edit_class_template.html', context)

@login_required
def edit_class_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        class_id = request.POST.get('class_id')
        class_name = request.POST.get('class')

        try:
            class1 = Class.objects.get(id=class_id)
            class1.class_name = class_name
            class1.save()

            messages.success(request, "class Updated Successfully.")
            return redirect('/edit_class/'+class_id)

        except:
            messages.error(request, "Failed to Update class.")
            return redirect('/edit_class/'+class_id)

@login_required
def delete_class(request, class_id):
    class1 = Class.objects.get(id=class_id)
    try:
        class1.delete()
        messages.success(request, "Class Deleted Successfully.")
        return redirect('manage_class')
    except:
        messages.error(request, "Failed to Delete class.")
        return redirect('manage_class')

@login_required
def manage_session(request):
    session_years = SessionYearModel.objects.all()
    context = {
        "session_years": session_years
    }
    return render(request, "hod_template/manage_session_template.html", context)

@login_required
def add_session(request):
    return render(request, "hod_template/add_session_template.html")

@login_required
def add_session_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_course')
    else:
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        try:
            sessionyear = SessionYearModel(session_start_year=session_start_year, session_end_year=session_end_year)
            sessionyear.save()
            messages.success(request, "Session Year added Successfully!")
            return redirect("add_session")
        except:
            messages.error(request, "Failed to Add Session Year")
            return redirect("add_session")

@login_required
def edit_session(request, session_id):
    session_year = SessionYearModel.objects.get(id=session_id)
    context = {
        "session_year": session_year
    }
    return render(request, "hod_template/edit_session_template.html", context)

@login_required
def edit_session_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('manage_session')
    else:
        session_id = request.POST.get('session_id')
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        try:
            session_year = SessionYearModel.objects.get(id=session_id)
            session_year.session_start_year = session_start_year
            session_year.session_end_year = session_end_year
            session_year.save()

            messages.success(request, "Session Year Updated Successfully.")
            return redirect('/edit_session/'+session_id)
        except:
            messages.error(request, "Failed to Update Session Year.")
            return redirect('/edit_session/'+session_id)

@login_required
def delete_session(request, session_id):
    session = SessionYearModel.objects.get(id=session_id)
    try:
        session.delete()
        messages.success(request, "Session Deleted Successfully.")
        return redirect('manage_session')
    except:
        messages.error(request, "Failed to Delete Session.")
        return redirect('manage_session')

@login_required
def add_student(request):
    class1=Class.objects.all()
    session1=SessionYearModel.objects.all()
    context = {
        "class1": class1,
        'session1':session1
    }
    return render(request, 'hod_template/add_student_template.html',context)



@login_required
def add_student_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_student')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone=request.POST.get('phone')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        class1=request.POST.get('class')
        session1=request.POST.get('session')
        father_name=request.POST.get('father_name')
        mother_name=request.POST.get('mother_name')
        myfile=request.FILES['myfile']

        try:
            user = Account.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            data=Account.objects.get(username=username)
            data.phone_number=phone
            data.dob=dob
            data.gender=gender
            data.father_name=father_name
            data.mother_name=mother_name
            data.image=myfile
            data.profile_type='student'
            data.save()

            #student model
            student=Students.objects.create(admin=user)
            student.address=address
            class_ob = Class.objects.get(id=class1)
            student.class_id = class_ob
            session_year_obj = SessionYearModel.objects.get(id=session1)
            student.session_year_id=session_year_obj
            student.save()

            
            
            messages.success(request, "Student Added Successfully!")
            return redirect('add_student')
        except:
            messages.error(request, "Failed to Add Student!")
            return redirect('add_student')

@login_required
def manage_student(request):
    students = Students.objects.all()
    context = {
        "students": students
    }
    return render(request, 'hod_template/manage_student_template.html', context)

@login_required
def edit_student(request, student_id):
    # Adding Student ID into Session Variable
    request.session['student_id'] = student_id
    student = Students.objects.get(admin=student_id)

    context = {
        "id": student_id,
        "username": student.admin.username,
        "student":student
    }
    return render(request, "hod_template/edit_student_template.html", context)

@login_required
def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone=request.POST.get('phone')
        father_name=request.POST.get('father_name')
        mother_name=request.POST.get('mother_name')
        student_id=request.POST.get("student_id")


        try:
            # INSERTING into Customuser Model
            user = Account.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.father_name=father_name
            user.mother_name=mother_name
            user.phone_number=phone
            user.save()
            
            # INSERTING into student Model
            student_model = Students.objects.get(admin=student_id)
            student_model.address = address
            student_model.save()

            messages.success(request, "student Updated Successfully.")
            return redirect('/edit_student/'+ student_id)

        except:
            messages.error(request, "Failed to Update student.")
            return redirect('/edit_student/'+ student_id)

@login_required
def delete_student(request, student_id):
    student = Students.objects.get(admin=student_id)
    try:
        student.delete()
        messages.success(request, "Student Deleted Successfully.")
        return redirect('manage_student')
    except:
        messages.error(request, "Failed to Delete Student.")
        return redirect('manage_student')

@login_required
def add_subject(request):
    class1 = Class.objects.all()
    teacher = Teacher.objects.all()
    context = {
        "classs": class1,
        "teachers":teacher
    }
    return render(request, 'hod_template/add_subject_template.html', context)


@login_required
def add_subject_save(request):
    if request.method != "POST":
        messages.error(request, "Method Not Allowed!")
        return redirect('add_subject')
    else:
        subject_name = request.POST.get('subject')
        class_id = request.POST.get('class')
        class1 = Class.objects.get(id=class_id)
        teacher_id = request.POST.get('teacher')
        teacher = Teacher.objects.get(id=teacher_id)
        try:
            subject = Subjects(subject_name=subject_name, class_id=class1, Teacher_id=teacher)
            subject.save()
            messages.success(request, "Subject Added Successfully!")
            return redirect('add_subject')
        except:
            messages.error(request, "Failed to Add Subject!")
            return redirect('add_subject')

@login_required
def manage_subject(request):
    subjects = Subjects.objects.all()
    context = {
        "subjects": subjects
    }
    return render(request, 'hod_template/manage_subject_template.html', context)

@login_required
def edit_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    class1 = Class.objects.all()
    teacher = Teacher.objects.all()
    context = {
        "subject": subject,
        "classs": class1,
        "teachers": teacher,
        "id": subject_id
    }
    return render(request, 'hod_template/edit_subject_template.html', context)

@login_required
def edit_subject_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method.")
    else:
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject')
        class_id = request.POST.get('class')
        teacher_id = request.POST.get('teacher')

        try:
            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name = subject_name

            class1 = Class.objects.get(id=class_id)
            subject.class_id = class1

            teacher =Teacher.objects.get(id=teacher_id)
            print(teacher)
            subject.Teacher_id =teacher
            subject.save()

            messages.success(request, "Subject Updated Successfully.")
            # return redirect('/edit_subject/'+subject_id)
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id}))

        except:
            messages.error(request, "Failed to Update Subject.")
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id}))
            # return redirect('/edit_subject/'+subject_id)


@login_required
def delete_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    try:
        subject.delete()
        messages.success(request, "Subject Deleted Successfully.")
        return redirect('manage_subject')
    except:
        messages.error(request, "Failed to Delete Subject.")
        return redirect('manage_subject')

@login_required
@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = Account.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = Account.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@login_required
def admin_profile(request):
    user = Account.objects.get(id=request.user.id)

    context={
        "user": user
    }
    return render(request, 'hod_template/admin_profile.html', context)

@login_required
def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = Account.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')
    
