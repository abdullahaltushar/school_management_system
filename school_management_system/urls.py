"""school_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from school_management_system import views
from school_management_system import HodViews
from school_management_system import TeacherViews
from school_management_system import StudentViews
from Account.views import logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Account.urls')),
    path('',views.home, name='home'),
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    path('admin_profile/', HodViews.admin_profile, name="admin_profile"),
    path('manage_teacher/', HodViews.manage_teacher, name="manage_teacher"),
    path('edit_teacher/<teacher_id>/', HodViews.edit_teacher, name="edit_teacher"),
    path('add_teacher/', HodViews.add_teacher, name="add_teacher"),
    path('manage_student/', HodViews.manage_student, name="manage_student"),
    path('add_student/', HodViews.add_student, name="add_student"),
    path('manage_class/', HodViews.manage_class, name="manage_class"),
    path('edit_class/<class_id>/', HodViews.edit_class, name="edit_class"),
    path('add_class/', HodViews.add_class, name="add_class"),
    path('add_subject/', HodViews.add_subject, name="add_subject"),
    path('manage_subject/', HodViews.manage_subject, name="manage_subject"),
    path('manage_session/', HodViews.manage_session, name="manage_session"),
    path('add_session/', HodViews.add_session, name="add_session"),
    path('logout_user/', logout, name="logout_user"),
    path('add_teacher_save/', HodViews.add_teacher_save, name="add_teacher_save"),
    path('check_email_exist/', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', HodViews.check_username_exist, name="check_username_exist"),
    path('delete_teacher/<teacher_id>/', HodViews.delete_teacher, name="delete_teacher"),
    path('edit_teacher_save/', HodViews.edit_teacher_save, name="edit_teacher_save"),
    path('add_class_save/', HodViews.add_class_save, name="add_class_save"),
    path('edit_class/<class_id>/', HodViews.edit_class, name="edit_class"),
    path('edit_class_save/', HodViews.edit_class_save, name="edit_class_save"),
    path('delete_class/<class_id>/', HodViews.delete_class, name="delete_class"),
    path('add_session_save/', HodViews.add_session_save, name="add_session_save"),
    path('edit_session/<session_id>', HodViews.edit_session, name="edit_session"),
    path('edit_session_save/', HodViews.edit_session_save, name="edit_session_save"),
    path('delete_session/<session_id>/', HodViews.delete_session, name="delete_session"),
    path('add_student_save/', HodViews.add_student_save, name="add_student_save"),
    path('edit_student/<student_id>', HodViews.edit_student, name="edit_student"),
    path('edit_student_save/', HodViews.edit_student_save, name="edit_student_save"),
    path('delete_student/<student_id>/', HodViews.delete_student, name="delete_student"),
    path('add_subject_save/', HodViews.add_subject_save, name="add_subject_save"),
    path('edit_subject/<subject_id>/', HodViews.edit_subject, name="edit_subject"),
    path('edit_subject_save/', HodViews.edit_subject_save, name="edit_subject_save"),
    path('delete_subject/<subject_id>/', HodViews.delete_subject, name="delete_subject"),
    path('admin_profile_update/', HodViews.admin_profile_update, name="admin_profile_update"),


    #teacher 

    path('teacher_home/', TeacherViews.Teacher_home, name="teacher_home"),
    path('teacher_profile/', TeacherViews.teacher_profile, name="teacher_profile"),
    path('teacher_profile_update/', TeacherViews.teacher_profile_update, name="teacher_profile_update"),
    path('teacher_add_result/', TeacherViews.teacher_add_result, name="teacher_add_result"),
    path('teacher_add_result_save/', TeacherViews.teacher_add_result_save, name="teacher_add_result_save"),
    #student
    path('student_home/', StudentViews.student_home, name="student_home"),
    path('student_profile/', StudentViews.student_profile, name="student_profile"),
    path('student_profile_update/', StudentViews.student_profile_update, name="student_profile_update"),
    path('student_view_result/', StudentViews.student_view_result, name="student_view_result"),
]
