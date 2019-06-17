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
    day1 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day2 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA') 
    day3 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day4 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day5 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')  
    day6 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day7 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day8 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day9 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')   
    day10 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day11 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day12 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day13 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day14 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day15 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day16 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day17 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day18 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day19 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day20 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day21 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day22 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day23 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day24 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day25 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day26 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day27 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day28 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day29 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day30 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    day31 = models.CharField(choices = ATTENDANCE_CHOICES,max_length = 100,default ='NA')
    

    

    def __str__(self):
        starting_date = str(self.starting_date)
        return starting_date



class SampleModel(models.Model):
    movie = models.CharField(max_length = 200)
    IMDB  = models.IntegerField()
    

    def __str__(self):
        return self.movie

