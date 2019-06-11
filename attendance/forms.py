from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Student
from attendance.models import CustomUser




class StudentSignUpForm(UserCreationForm):
   
    class Meta(UserCreationForm.Meta):
        model =CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
        )
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user,name = str(str(user.first_name) + " " + str(user.last_name) ))
        return user


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user

