from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import Student
from django.contrib.auth import login
from .models import User
from django.views.generic import CreateView
from .models import CustomUser,Attendance
from .forms import StudentSignUpForm,TeacherSignUpForm
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def is_staff(user):
    object = CustomUser.objects.get(id = user.id)
    if object.is_teacher == True:
        return True
    else:
        return False

def is_student_teacher_admin(user):
    pass

@login_required
@user_passes_test(is_staff)
def StudentList(request):
    students= Student.objects.all()
    attendances = Attendance.objects.all()
    return render(request,'StudentList.html',{'students':students,'attendances':attendances})

@login_required

def StudentAttendance(request,pk):
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




