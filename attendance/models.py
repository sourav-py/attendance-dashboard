from django.db import models
from django.contrib.auth.models import AbstractUser,User
from datetime import datetime

# Create your models here.
def get_year():
    temp = datetime.now()
    temp2 = temp.year
    return temp2

class CustomUser(AbstractUser):
   is_student = models.BooleanField(default=False)
   is_teacher = models.BooleanField(default=False)

   def __str__(self):
       return self.username
    

class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete = models.CASCADE,default = 1)
    name = models.CharField(max_length = 100)
 

    def __str__(self):
        return self.user.username

  
    @property
    def total_attendance(self):
        return 5


class Week(models.Model):
    MonthChoices = (
        ('January','Jan'),
        ('February','Feb'),
        ('March','Mar'),
        ('April','Apr'),
        ('May','May'),
        ('June','Jun'),
        ('July','Jul'),
        ('August','Aug'),
        ('September','Sep'),
        ('October','Oct'),
        ('November','Nov'),
        ('December','Dec'),

    )
    month = models.CharField(choices = MonthChoices,max_length = 100)
    starting_date = models.DateField(default = datetime.now)
    year = models.DateTimeField(default = get_year)


  
    
class Attendance(models.Model):
    ATTENDANCE_CHOICES = (('Present','P'),('Absent','A'),('NA','NA'))
    MonthChoices = (
        ('January','Jan'),
        ('February','Feb'),
        ('March','Mar'),
        ('April','Apr'),
        ('May','May'),
        ('June','Jun'),
        ('July','Jul'),
        ('August','Aug'),
        ('September','Sep'),
        ('October','Oct'),
        ('November','Nov'),
        ('December','Dec'),

    )
    month = models.CharField(choices = MonthChoices,max_length = 100)
    year = models.BigIntegerField(default = get_year)
    starting_date = models.DateField(default = datetime.now)
    user = models.ManyToManyField(Student)
    monday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'P')
    tuesday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'P')
    wednesday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'P')
    thursday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'P')
    friday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'P')
    saturday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'P')


    def __str__(self):
        return self.month
