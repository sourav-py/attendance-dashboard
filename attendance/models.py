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


    
class Attendance(models.Model):
    ATTENDANCE_CHOICES = (('Present','P'),('Absent','A'),('NA','NA')) 
    starting_date = models.DateField(default = datetime.now)
    user = models.ManyToManyField(Student)
    monday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'NA')
    tuesday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'NA')
    wednesday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'NA')
    thursday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'NA')
    friday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'NA')
    saturday = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 10,default = 'NA')


    def __str__(self):
        starting_date = str(self.starting_date)
        return starting_date



class SampleModel(models.Model):
    movie = models.CharField(max_length = 200)
    IMDB  = models.IntegerField()
    

    def __str__(self):
        return self.movie

