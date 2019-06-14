from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import Student
from django.contrib.auth import login
from .models import User,SampleModel
from django.views.generic import CreateView
from .models import CustomUser,Attendance
from .forms import StudentSignUpForm,TeacherSignUpForm
from django.contrib.auth.decorators import login_required, user_passes_test
from tablib import Dataset
from .resources import SampleModelResource
import pandas as pd
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from attendance.serializers import SampleModelSerializer

def is_staff(user):
    object = CustomUser.objects.get(id = user.id)
    if object.is_teacher == True:
        return True
    else:
        return False

def is_student_teacher_admin(user):
    pass

@login_required
#@user_passes_test(is_staff)
def StudentList(request):
    """
        Lists all the students in the database with their attendance link available for the teacher or the student itself.
    """
    students= Student.objects.all()
    attendances = Attendance.objects.all()
    return render(request,'StudentList.html',{'students':students,'attendances':attendances})

@login_required

def StudentAttendance(request,pk):
    """
        overview of the attendance of student(can be opened by the teacher or the student itself)
    """
    student = Student.objects.get(id = pk)
    attendances = Attendance.objects.filter(user = student)
    if request.user.is_teacher == True or request.user == student.user:
        return render(request,'StudentAttendance.html',{'student':student,'attendances':attendances})
    else:
        return HttpResponse('You can\' access this')



class StudentSignUpView(CreateView):
    model = CustomUser
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form_student.html'
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return HttpResponseRedirect('/')


class TeacherSignUpView(CreateView):
    model = CustomUser
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form_teacher.html'

    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect('/students/')


def Sample_Model_Csv_Upload(request):
    """
        uploads csv file of Sample Model and stores it in database
    """
    if request.method == 'POST':
       
        csvfile = request.FILES['myfile']
        data = pd.read_csv(csvfile)
        for i in data.values:
            id = i[0]
            movie = i[1]
            imdb = i[2]
            print(id,movie,imdb)
            new_sample_object = SampleModel.objects.create(movie = movie,IMDB = imdb)
            new_sample_object.save()
        return HttpResponse('Check shell!')
    

    return render(request, 'sample_model_csv_upload.html')

def Student_Csv_Upload(request):
    """
        uploads csv file of students and stores it in database
    """
    initial_users_list = []
    if request.method == 'POST':
        csvfile = request.FILES['myfile']
        data = pd.read_csv(csvfile)
        for i in data.values:
            username = i[0]
            password = i[1]
            first_name = i[2]
            last_name = i[3]
            #check if it is already present in db
            initial_users = CustomUser.objects.all()
            for user in initial_users:
                initial_users_list.append(str(user.username))
            if username not in initial_users_list:    
                print(username,password,first_name,last_name)
                new_user_object = CustomUser.objects.create_user(username = username,password=password,first_name = first_name,last_name = last_name,is_student = True)
                new_user_object = authenticate(username=username,password=password)
                new_user_object.save()
                student_object = Student.objects.create(user = new_user_object,name=str(str(first_name)+" "+str(last_name)))
                student_object.save()
            
        return HttpResponseRedirect('/students/')
    

    return render(request, 'student_csv_upload.html')

def Attendance_Csv_Upload(request):
    initial_attendance_list = []
    if request.method == 'POST':
        csvfile = request.FILES['myfile']
        data = pd.read_csv(csvfile)
        for i in data.values:
            starting_date = i[0]
            username = i[1]
            monday = i[2]
            tuesday = i[3]
            wednesday = i[4]
            thursday = i[5]
            friday = i[6]
            saturday = i[7]
            new_attendance_object = Attendance.objects.create(starting_date = starting_date,monday = monday,tuesday = tuesday,wednesday = wednesday,thursday=thursday,friday=friday,saturday=saturday)
            new_attendance_object.user.add(Student.objects.get(user=CustomUser.objects.get(username = username)))
            new_attendance_object.save()
            
        return HttpResponseRedirect('/students/')
    

    return render(request, 'student_csv_upload.html')





#----------------------API views-------------------------------

reciever_list = []
@api_view(['GET','POST'])
def SampleModelEndpoint(request):

    if request.method == 'GET':
        sample = reciever_list[1]
        sample2 = reciever_list[2]
        response = str(sample) + str(sample2)
        return HttpResponse(response)
    if request.method == 'POST':
        movie = request.post('movie')
        IMDB = request.post('IMDB')
        reciever_list.append(str(movie))
        reciever_list.append(str(IMDB))
    




