from django.urls import path
from attendance import views
from django.conf.urls import url

urlpatterns = [
    #--------------general urls ------------------------------
    path('',views.base,name = 'base'),
    path('students/',views.StudentList,name = 'StudentList'), 
    url(r'^student-attendance/(?P<pk>[0-9]+)/$', views.StudentAttendance,name = 'StudentAttendance'),


    #--------------csvupload--------------------------------
    path('upload/csv/students/',views.Student_Csv_Upload),
    path('upload/csv/attendance/',views.Attendance_Csv_Upload),


    #--------------endpoints-----------------------------
    path('api-view/samplemodel/',views.SampleModelEndpoint),
    path('api-view/studentmodel/',views.StudentModelEndpoint),
    


    #-------------accounts-----------------------------------
    path('login/student/',views.login_student),
    path('login/teacher/',views.login_teacher),
    path('accounts/signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),
 

]
