from django.urls import path
from attendance import views
from django.conf.urls import url

urlpatterns = [
    path('students/',views.StudentList,name = 'StudentList'),
    path('accounts/signup/student/', views.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', views.TeacherSignUpView.as_view(), name='teacher_signup'),  
    url(r'^student-attendance/(?P<pk>[0-9]+)/$', views.StudentAttendance,name = 'StudentAttendance'),
    path('upload/csv/SampleModel/',views.simple_upload,name = 'simple_upload'),

]