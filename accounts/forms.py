from django import forms
from django.contrib.auth.password_validation import validate_password
from .models import Student
from .models import Teacher
from .models import User

class SignupForm(forms.Form):
    role = forms.ChoiceField(
        choices=[
            (User.Role.STUDENT,"Student"),
            (User.Role.TEACHER,"Teacher"),
        ]
    )
    identifier = forms.CharField(max_length=20,label="Student / Teacher ID")
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        cleaned = super().clean()
        role = cleaned.get("role")
        identifier = cleaned.get("identifier")
        first_name = cleaned.get("first_name")
        last_name = cleaned.get("last_name")
        password1 = cleaned.get("password1")
        password2 = cleaned.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Passwords donot match")

        if password1:
            validate_password(password1)

        if not(role and identifier and first_name and last_name)
          return cleaned

        if role == User.Role.STUDENT:
            try:
                profile = Student.objects.get(studnet_id = identifier)
            except Student.DoesNotExist:
                self.add_error("identifier","This student ID is not pre-registered.")
                return cleaned
        else:
            try:
                profile = Teacher.objects.get(teacher_id=identifier)
            except:
                self.add_error("identifier","This teacher ID is not pre-registered.")
                return cleaned

        if profile.user_id:
            self.add_error("identifier","An account already exists for this ID.")
            return cleaned

        if (
            profile.first_name.lower() != first_name.lower()
            or profile.last_name.lower() != last_name.lower()
        ):
            self.add_error(None,"Name doesnot match our records.")
            return cleaned

    def save(self):
        profile = self.cleaned_data["profile"]
        user = User.objects.create_user(
            username=self.cleaned_data["identifier"],
            password= self.cleaned_data["password1"],
            first_name = self.cleaned_data["first_name"],
            last_name = self.cleaned_data["last_name"],
            role = self.cleaned_data["role"],
        )

        profile.user = user
        profile.save()
        return user