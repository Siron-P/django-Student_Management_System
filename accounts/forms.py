from django import forms
from django.contrib.auth.password_validation import validate_password

from students.models import Student
from teachers.models import Teacher
from .models import User
from courses.models import Course

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
            try:
                validate_password(password1)
            except forms.ValidationError as e:
                self.add_error("password1",e)

        if not(role and identifier and first_name and last_name):
          return cleaned

        if role == User.Role.STUDENT:
            try:
                profile = Student.objects.get(student_id = identifier)
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

        cleaned["profile"] = profile
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

class PreregisterForm(forms.Form):
    role = forms.ChoiceField(
        choices=[
            (User.Role.STUDENT,"Student"),
            (User.Role.TEACHER,"Teacher"),
        ]
    )
    identifier = forms.CharField(max_length=20, label="Student / Teacher ID")
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    course = forms.ModelChoiceField(
        queryset = Course.objects.all(),required= False,
        label="Course (for students)"
    )

    semester = forms.ChoiceField(
        choices=[("","Select Semester")]+list(Student.Semester.choices),
        required=False,label="Semester (for student)"
    )

    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(), required=False,
        label="Courses (for teacher)"
    )

    def clean(self):
        cleaned = super().clean()
        role = cleaned.get("role")
        identifier = cleaned.get("identifier")

        if role and identifier:
            if role == User.Role.STUDENT and Student.objects.filter(student_id=identifier).exists():
                self.add_error("identifier", "This student ID is already registered.")
            elif role == User.Role.TEACHER and Teacher.objects.filter(teacher_id=identifier).exists():
                self.add_error("identifier", "This teacher ID is already registered.")

        return cleaned

    def save(self):
        role = self.cleaned_data["role"]
        identifier = self.cleaned_data["identifier"]
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]

        if role == User.Role.STUDENT:
            student = Student.objects.create(
                student_id = identifier, first_name= first_name,last_name=last_name,
                course = self.cleaned_data.get("course"),
                semester = self.cleaned_data.get("semester"),
            )
            return student
        else:
            teacher = Teacher.objects.create(
                teacher_id = identifier,first_name=first_name,last_name= last_name,
            )
            selected_courses = self.cleaned_data.get("courses")
            if selected_courses:
                teacher.courses.set(selected_courses)
            return teacher