from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,Http404
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
from datetime import datetime

from attendance.serializers import SampleModelSerializer
from django.views.decorators.cache import never_cache,cache_control

def is_staff(user):
    object = CustomUser.objects.get(id = user.id)
    if object.is_teacher == True:
        return True
    else:
        return False

def is_student_teacher_admin(user):
    pass

def count_attendance(id):
    count = 0
    student_object = Student.objects.get(id = id)
    attendances = Attendance.objects.filter(user = student_object)
    for attendance in attendances:
        if attendance.day1 == 'Present':
            count += 1
        if attendance.day2 == 'Present':
            count += 1
        if attendance.day3 == 'Present':
            count += 1
        if attendance.day4 == 'Present':
            count +=1
        if attendance.day5 == 'Present':
            count +=1
        if attendance.day6 == 'Present':
            count +=1
        if attendance.day7 == 'Present':
            count += 1
        if attendance.day8 == 'Present':
            count += 1
        if attendance.day9 == 'Present':
            count += 1
        if attendance.day10 == 'Present':
            count +=1
        if attendance.day11 == 'Present':
            count +=1
        if attendance.day12 == 'Present':
            count +=1
        if attendance.day13 == 'Present':
            count += 1
        if attendance.day14 == 'Present':
            count += 1
        if attendance.day15 == 'Present':
            count += 1
        if attendance.day16 == 'Present':
            count +=1
        if attendance.day17 == 'Present':
            count +=1
        if attendance.day18 == 'Present':
            count +=1
        if attendance.day19 == 'Present':
            count += 1
        if attendance.day20 == 'Present':
            count += 1
        if attendance.day21 == 'Present':
            count += 1
        if attendance.day22 == 'Present':
            count +=1
        if attendance.day23 == 'Present':
            count +=1
        if attendance.day24 == 'Present':
            count +=1
        if attendance.day25 == 'Present':
            count += 1
        if attendance.day26 == 'Present':
            count += 1
        if attendance.day27 == 'Present':
            count += 1
        if attendance.day28 == 'Present':
            count +=1
        if attendance.day29 == 'Present':
            count +=1
        if attendance.day30 == 'Present':
            count +=1
        if attendance.day31 == 'Present':
            count +=1
    return count


def out_of_attendance(id):
    count = 0
    student_object = Student.objects.get(id = id)
    attendances = Attendance.objects.filter(user = student_object)
    for attendance in attendances:
        if attendance.day1 == 'Present' or attendance.day1 == 'Absent':
            count += 1
        if attendance.day2 == 'Present' or attendance.day2 == 'Absent':
            count += 1
        if attendance.day3 == 'Present' or attendance.day3 == 'Absent':
            count += 1
        if attendance.day4 == 'Present' or attendance.day4 == 'Absent':
            count +=1
        if attendance.day5 == 'Present' or attendance.day5 == 'Absent':
            count +=1
        if attendance.day6 == 'Present' or attendance.day6 == 'Absent':
            count +=1
        if attendance.day7 == 'Present' or attendance.day7 == 'Absent':
            count += 1
        if attendance.day8 == 'Present' or attendance.day8 == 'Absent':
            count += 1
        if attendance.day9 == 'Present' or attendance.day9 == 'Absent':
            count += 1
        if attendance.day10 == 'Present' or attendance.day10 == 'Absent':
            count +=1
        if attendance.day11 == 'Present' or attendance.day11 == 'Absent':
            count +=1
        if attendance.day12 == 'Present' or attendance.day12 == 'Absent':
            count +=1
        if attendance.day13 == 'Present' or attendance.day13 == 'Absent':
            count += 1
        if attendance.day14 == 'Present' or attendance.day14 == 'Absent':
            count += 1
        if attendance.day15 == 'Present' or attendance.day15 == 'Absent':
            count += 1
        if attendance.day16 == 'Present' or attendance.day16 == 'Absent':
            count +=1
        if attendance.day17 == 'Present' or attendance.day17 == 'Absent':
            count +=1
        if attendance.day18 == 'Present' or attendance.day18 == 'Absent':
            count +=1
        if attendance.day19 == 'Present' or attendance.day19 == 'Absent':
            count += 1
        if attendance.day20 == 'Present' or attendance.day20 == 'Absent':
            count += 1
        if attendance.day21 == 'Present' or attendance.day21 == 'Absent':
            count += 1
        if attendance.day22 == 'Present' or attendance.day22 == 'Absent':
            count +=1
        if attendance.day23 == 'Present' or attendance.day23 == 'Absent':
            count +=1
        if attendance.day24 == 'Present' or attendance.day24 == 'Absent':
            count +=1
        if attendance.day25 == 'Present' or attendance.day25 == 'Absent':
            count += 1
        if attendance.day26 == 'Present' or attendance.day26 == 'Absent':
            count += 1
        if attendance.day27 == 'Present' or attendance.day27 == 'Absent':
            count += 1
        if attendance.day28 == 'Present' or attendance.day28 == 'Absent':
            count +=1
        if attendance.day29 == 'Present' or attendance.day29 == 'Absent':
            count +=1
        if attendance.day30 == 'Present' or attendance.day30 == 'Absent':
            count +=1
        if attendance.day31 == 'Present' or attendance.day31 == 'Absent':
            count +=1
    return count



def base(request):
    return render(request,'base.html',{'request':request})



@login_required
@user_passes_test(is_staff)
def StudentList(request):
    message = ""
    students= Student.objects.all()
    try:
        Student.objects.get(id=1)
    except:
        message += "NO STUDENTS IN DB"
    attendances = Attendance.objects.all()
    return render(request,'StudentList.html',{'students':students,'attendances':attendances,'request':request,'message':message})

@login_required
def StudentAttendance(request,pk):
    student = Student.objects.get(id = pk)
    attendances = Attendance.objects.filter(user = student)
    if request.user.is_teacher == True or request.user == student.user:
        attendance_variable = count_attendance(pk)
        out_of_attendance_variable = out_of_attendance(pk)
        if out_of_attendance_variable == 0:
            attendance_percentage = 0
        else:
            attendance_percentage = (attendance_variable/out_of_attendance_variable)*100
        if attendance_percentage < 75 and out_of_attendance_variable != 0:
            message = "WARNING : your attendance is below 75%, you are expected to have more than 75% to sit in exams!!!"
        else:
            message = ""
        return render(request,'StudentAttendance.html',{'student':student,'attendances':attendances,'attendance_variable':attendance_variable,'out_of_attendance_variable':out_of_attendance_variable,'attendance_percentage':attendance_percentage,'message':message})
    else:
        return HttpResponse('You can\'t access this')


def login_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_student == True:
            if user.is_active:
                login(request, user)
                student_object_id = Student.objects.get(user = user).id
                return HttpResponseRedirect('/student-attendance/%s'%(student_object_id))
                
        else:
            whose_login = "student login page"
            message = "please enter correct credentials(student's creds.)"
            return render(request,'registration/login.html',{'request':request,'message':message,'whose_login':whose_login})
    else:
        whose_login = "student login page"
        return render(request,'registration/login.html',{'request':request,'whose_login':whose_login})


def login_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_teacher == True:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/students/')
        else:
            whose_login = "teacher login page"
            message = "please enter correct credentials(teacher's creds.)"
            return render(request,'registration/login.html',{'request':request,'message':message,'whose_login':whose_login})
    else:
        whose_login = "teacher login page"
        return render(request,'registration/login.html',{'request':request,'whose_login':whose_login})
        

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
    initial_users_list = []
    if request.method == 'POST':
        csvfile = request.FILES['myfile']
        data = pd.read_csv(csvfile)
        for i in data.values:
            username = i[0]
            password = i[2]
            first_name = i[1]
            last_name = ''
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

    if request.method == 'POST':
        initial_attendance_list = []
        csvfile = request.FILES['myfile']
        data = pd.read_csv(csvfile)
        datetime_var = datetime.now()
        date = datetime_var.day
        month = datetime_var.month


        username_list = []
        attendance_list = []

        for i in data['ID']:
            username_list.append(str(i))
        for i in data["Day  "+str(date)]:
            attendance_list.append(str(i))

        k = 0
        for i in range(0,len(data['ID'])):
            if str(attendance_list[i]) != 'nan':
                k = k+1
        if k!= 0:
            
            for i in range(0,len(data['ID'])):
                
                username = username_list[i]
                attendance_temp = attendance_list[i]
                if str(attendance_temp) == 'nan':
                    attendance = 'Absent'
                else:
                    attendance = attendance_temp
                day = 'day' + str(date)
                month = str(month)

                initial_attendance_objects = Attendance.objects.all()
                for i in initial_attendance_objects:
                    
                    sample = ""
                    for j in i.user.all():
                        sample += str(j.user.username)
                    
                    sample2 = str(i.month) + str(sample)
                    initial_attendance_list.append(sample2)
                sample3 = str(month) + str(username)
                if sample3 not in initial_attendance_list:
                    new_attendance_object = Attendance.objects.create(month = month)
                    try:
                        new_attendance_object.user.add(Student.objects.get(user=CustomUser.objects.get(username = username)))
                    except:
                        raise Http404
                    if day == 'day1':
                        new_attendance_object.day1 = str(attendance)
                    if day == 'day2':
                        new_attendance_object.day2 = str(attendance)
                    if day == 'day3':
                        new_attendance_object.day3 = str(attendance)
                    if day == 'day4':
                        new_attendance_object.day4 = str(attendance)
                    if day == 'day5':
                        new_attendance_object.day5 = str(attendance)
                    if day == 'day6':
                        new_attendance_object.day6 = str(attendance)
                    if day == 'day7':
                        new_attendance_object.day7 = str(attendance)
                    if day == 'day8':
                        new_attendance_object.day8 = str(attendance)
                    if day == 'day9':
                        new_attendance_object.day9 = str(attendance)
                    if day == 'day10':
                        new_attendance_object.day10 = str(attendance)
                    if day == 'day11':
                        new_attendance_object.day11 = str(attendance)
                    if day == 'day12':
                        new_attendance_object.day12 = str(attendance)
                    if day == 'day13':
                        new_attendance_object.day13 = str(attendance)
                    if day == 'day14':
                        new_attendance_object.day14 = str(attendance)
                    if day == 'day15':
                        new_attendance_object.day15 = str(attendance)
                    if day == 'day16':
                        new_attendance_object.day16 = str(attendance)
                    if day == 'day17':
                        new_attendance_object.day17 = str(attendance)
                    if day == 'day18':
                        new_attendance_object.day18 = str(attendance)
                    if day == 'day19':
                        new_attendance_object.day19 = str(attendance)
                    if day == 'day20':
                        new_attendance_object.day20 = str(attendance)
                    if day == 'day21':
                        new_attendance_object.day21 = str(attendance)
                    if day == 'day22':
                        new_attendance_object.day22 = str(attendance)
                    if day == 'day23':
                        new_attendance_object.day23 = str(attendance)
                    if day == 'day24':
                        new_attendance_object.day24 = str(attendance)
                    if day == 'day25':
                        new_attendance_object.day25 = str(attendance)
                    if day == 'day26':
                        new_attendance_object.day26 = str(attendance)
                    if day == 'day27':
                        new_attendance_object.day27 = str(attendance)
                    if day == 'day28':
                        new_attendance_object.day28 = str(attendance)
                    if day == 'day29':
                        new_attendance_object.day29 = str(attendance)
                    if day == 'day30':
                        new_attendance_object.day30 = str(attendance)
                    if day == 'day31':
                        new_attendance_object.day31 = str(attendance)
                    new_attendance_object.save()
                    
                    
                    
                        
                else:
                    for i in Attendance.objects.all():
                        sample= ""
                        for j in i.user.all():
                            sample += str(j.user.username)
                        if sample == username and i.month == month:
                            update_attendance_object = i
            
                    
                    
                    if day == 'day1':
                        update_attendance_object.day1 = str(attendance)
                    if day == 'day2':
                        update_attendance_object.day2 = str(attendance)
                    if day == 'day3':
                        update_attendance_object.day3 = str(attendance)
                    if day == 'day4':
                        update_attendance_object.day4 = str(attendance)
                    if day == 'day5':
                        update_attendance_object.day5 = str(attendance)
                    if day == 'day6':
                        update_attendance_object.day6 = str(attendance)
                    if day == 'day7':
                        update_attendance_object.day7 = str(attendance)
                    if day == 'day8':
                        update_attendance_object.day8 = str(attendance)
                    if day == 'day9':
                        update_attendance_object.day9 = str(attendance)
                    if day == 'day10':
                        update_attendance_object.day10 = str(attendance)
                    if day == 'day11':
                        update_attendance_object.day11 = str(attendance)
                    if day == 'day12':
                        update_attendance_object.day12 = str(attendance)
                    if day == 'day13':
                        update_attendance_object.day13 = str(attendance)
                    if day == 'day14':
                        update_attendance_object.day14 = str(attendance)
                    if day == 'day15':
                        update_attendance_object.day15 = str(attendance)
                    if day == 'day16':
                        update_attendance_object.day16 = str(attendance)
                    if day == 'day17':
                        update_attendance_object.day17 = str(attendance)
                    if day == 'day18':
                        update_attendance_object.day18 = str(attendance)
                    if day == 'day19':
                        update_attendance_object.day19 = str(attendance)
                    if day == 'day20':
                        update_attendance_object.day20 = str(attendance)
                    if day == 'day21':
                        update_attendance_object.day21 = str(attendance)
                    if day == 'day22':
                        update_attendance_object.day22 = str(attendance)
                    if day == 'day23':
                        update_attendance_object.day23 = str(attendance)
                    if day == 'day24':
                        update_attendance_object.day24 = str(attendance)
                    if day == 'day25':
                        update_attendance_object.day25 = str(attendance)
                    if day == 'day26':
                        update_attendance_object.day26 = str(attendance)
                    if day == 'day27':
                        update_attendance_object.day27 = str(attendance)
                    if day == 'day28':
                        update_attendance_object.day28 = str(attendance)
                    if day == 'day29':
                        update_attendance_object.day29 = str(attendance)
                    if day == 'day30':
                        update_attendance_object.day30 = str(attendance)
                    if day == 'day31':
                        update_attendance_object.day31 = str(attendance)
                    update_attendance_object.save()
                    
                    
                    
        return HttpResponseRedirect('/students/')
                

    return render(request, 'student_csv_upload.html')




#----------------------API views-------------------------------


@api_view(['GET','POST'])
def SampleModelEndpoint(request):
    initial_movies_list = []
    if request.method == 'POST':
        movie = request.data['movie']
        IMDB = request.data['IMDB']
        initial_movies = SampleModel.objects.all()
        for movie in initial_movies:
            initial_movies_list.append(movie.movie)
        if movie not in initial_movies_list:
            new_sample_object = SampleModel.objects.create(movie = movie,IMDB = IMDB)
            new_sample_object.save()
            return HttpResponse('Your model is saved!')   

@api_view(['GET','POST'])
def StudentModelEndpoint(request):
    initial_users_list = []
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        initial_users = CustomUser.objects.all()
        for user in initial_users:
            initial_users_list.append(str(user.username))
        if username not in initial_users_list:    
            new_user_object = CustomUser.objects.create_user(username = username,password=password,first_name = first_name,last_name = last_name,is_student = True)
            new_user_object = authenticate(username=username,password=password)
            new_user_object.save()
            student_object = Student.objects.create(user = new_user_object,name=str(str(first_name)+" "+str(last_name)))
            student_object.save()

@api_view(['GET','POST'])
def AttendanceModelEndPoint(request):
    if request.method == 'POST':
        initial_attendance_list = []
        
        
        username = request.data['username']
        attendance = request.data['attendance']
        month = request.data['month']
        day = request.data['day']
        
        initial_attendance_objects = Attendance.objects.all()
        for i in initial_attendance_objects:
            
            sample = ""
            for j in i.user.all():
                sample += str(j.user.username)
            
            sample2 = str(i.month) + str(sample)
            initial_attendance_list.append(sample2)
        sample3 = str(month) + str(username)
        if sample3 not in initial_attendance_list:
            new_attendance_object = Attendance.objects.create(month = month)
            new_attendance_object.user.add(Student.objects.get(user=CustomUser.objects.get(username = username)))
            if day == 'day1':
                new_attendance_object.day1 = str(attendance)
            if day == 'day2':
                new_attendance_object.day2 = str(attendance)
            if day == 'day3':
                new_attendance_object.day3 = str(attendance)
            if day == 'day4':
                new_attendance_object.day4 = str(attendance)
            if day == 'day5':
                new_attendance_object.day5 = str(attendance)
            if day == 'day6':
                new_attendance_object.day6 = str(attendance)
            if day == 'day7':
                new_attendance_object.day7 = str(attendance)
            if day == 'day8':
                new_attendance_object.day8 = str(attendance)
            if day == 'day9':
                new_attendance_object.day9 = str(attendance)
            if day == 'day10':
                new_attendance_object.day10 = str(attendance)
            if day == 'day11':
                new_attendance_object.day11 = str(attendance)
            if day == 'day12':
                new_attendance_object.day12 = str(attendance)
            if day == 'day13':
                new_attendance_object.day13 = str(attendance)
            if day == 'day14':
                new_attendance_object.day14 = str(attendance)
            if day == 'day15':
                new_attendance_object.day15 = str(attendance)
            if day == 'day16':
                new_attendance_object.day16 = str(attendance)
            if day == 'day17':
                new_attendance_object.day17 = str(attendance)
            if day == 'day18':
                new_attendance_object.day18 = str(attendance)
            if day == 'day19':
                new_attendance_object.day19 = str(attendance)
            if day == 'day20':
                new_attendance_object.day20 = str(attendance)
            if day == 'day21':
                new_attendance_object.day21 = str(attendance)
            if day == 'day22':
                new_attendance_object.day22 = str(attendance)
            if day == 'day23':
                new_attendance_object.day23 = str(attendance)
            if day == 'day24':
                new_attendance_object.day24 = str(attendance)
            if day == 'day25':
                new_attendance_object.day25 = str(attendance)
            if day == 'day26':
                new_attendance_object.day26 = str(attendance)
            if day == 'day27':
                new_attendance_object.day27 = str(attendance)
            if day == 'day28':
                new_attendance_object.day28 = str(attendance)
            if day == 'day29':
                new_attendance_object.day29 = str(attendance)
            if day == 'day30':
                new_attendance_object.day30 = str(attendance)
            if day == 'day31':
                new_attendance_object.day31 = str(attendance)
            new_attendance_object.save()
            
            
            
                
        else:
            
            for i in Attendance.objects.all():
                sample= ""
                for j in i.user.all():
                    sample += str(j.user.username)
                if sample == username and i.month == month:
                    update_attendance_object = i
            if day == 'day1':
                update_attendance_object.day1 = str(attendance)
            if day == 'day2':
                update_attendance_object.day2 = str(attendance)
            if day == 'day3':
                update_attendance_object.day3 = str(attendance)
            if day == 'day4':
                update_attendance_object.day4 = str(attendance)
            if day == 'day5':
                update_attendance_object.day5 = str(attendance)
            if day == 'day6':
                update_attendance_object.day6 = str(attendance)
            if day == 'day7':
                update_attendance_object.day7 = str(attendance)
            if day == 'day8':
                update_attendance_object.day8 = str(attendance)
            if day == 'day9':
                update_attendance_object.day9 = str(attendance)
            if day == 'day10':
                update_attendance_object.day10 = str(attendance)
            if day == 'day11':
                update_attendance_object.day11 = str(attendance)
            if day == 'day12':
                update_attendance_object.day12 = str(attendance)
            if day == 'day13':
                update_attendance_object.day13 = str(attendance)
            if day == 'day14':
                update_attendance_object.day14 = str(attendance)
            if day == 'day15':
                update_attendance_object.day15 = str(attendance)
            if day == 'day16':
                update_attendance_object.day16 = str(attendance)
            if day == 'day17':
                update_attendance_object.day17 = str(attendance)
            if day == 'day18':
                update_attendance_object.day18 = str(attendance)
            if day == 'day19':
                update_attendance_object.day19 = str(attendance)
            if day == 'day20':
                update_attendance_object.day20 = str(attendance)
            if day == 'day21':
                update_attendance_object.day21 = str(attendance)
            if day == 'day22':
                update_attendance_object.day22 = str(attendance)
            if day == 'day23':
                update_attendance_object.day23 = str(attendance)
            if day == 'day24':
                update_attendance_object.day24 = str(attendance)
            if day == 'day25':
                update_attendance_object.day25 = str(attendance)
            if day == 'day26':
                update_attendance_object.day26 = str(attendance)
            if day == 'day27':
                update_attendance_object.day27 = str(attendance)
            if day == 'day28':
                update_attendance_object.day28 = str(attendance)
            if day == 'day29':
                update_attendance_object.day29 = str(attendance)
            if day == 'day30':
                update_attendance_object.day30 = str(attendance)
            if day == 'day31':
                update_attendance_object.day31 = str(attendance)
            update_attendance_object.save()
            
            
            
        return HttpResponse('post request process done......cheese!')
        
    if request.method == 'GET':
        sample = str(initial_attendance_list[0])
        return HttpResponse(sample)



@api_view(['GET','POST'])
def DeleteEndpoint(request):
    if request.method == 'POST':
        username = request.data['username']
        for i in CustomUser.objects.all():
            if i.username == username:
                i.delete()





         




           

    




