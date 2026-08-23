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
    name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20, unique=True)
    courses = models.ManyToManyField(Course, related_name="teahcers",blank= True)

    def __str__(self):
        return self.name