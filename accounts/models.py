from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN","Admin"
        TEACHER ="TEAHCER","Teacher"
        STUDENT = "STUDENT","Student"

    role = models.CharField(max_length=10, choices=Role.choices)

    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser

    def is_teacher(self):
        return self.role == self.Role.TEAHCER

    def is_student(self):
        return self.role == self.Role.STUDENT

    def __str__(self):
        return f"{self.username} ({self.role})"