from django.db import models
from django.conf import settings
from courses.models import Course

class Teahcer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        null=True,
        blank=True,
        related_name="teacher_profile",
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    teacher_id = models.CharField(max_length=20, unique=True)
    courses = models.ManyToManyField(Course, related_name="teahcers",blank= True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"