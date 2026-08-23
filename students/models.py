from django.db import models
from django.conf import settings
from courses.models import Course


class Student(models.Model):
    class Semester(models.TextChoices):
        SEM1 = "1", "Sem 1"
        SEM2 = "2", "Sem 2"
        SEM3 = "3", "Sem 3"
        SEM4 = "4", "Sem 4"
        SEM5 = "5", "Sem 5"
        SEM6 = "6", "Sem 6"
        SEM7 = "7", "Sem 7"
        SEM8 = "8", "Sem 8"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="student_profile",
    )

    # --- filled by ADMIN at registration ---
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_id = models.CharField(max_length=20, unique=True)
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, null=True, blank=True, related_name="students"
    )
    semester = models.CharField(max_length=1, choices=Semester.choices, blank=True)

    # --- filled by STUDENT later, via complete_profile page ---
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, blank=True)

    profile_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"