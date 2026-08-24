from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from .models import User

class StudentSignupCheckForm(forms.Form):
    student_id = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder':'Username'
        })

        self.fields['email'].widget.attrs.update({
            'placeholder':'Email'
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder':'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder':'Confirm Password'
        })

