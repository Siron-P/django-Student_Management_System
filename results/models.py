from django.db import models
from students.models import Student
from courses.models import Course

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="results")
    marks_obtained = models.DecimalField(max_digits=5,decimal_places=2)
    max_marks = models.DecimalField(max_digits=5,decimal_places=2, default=100)
    exam_type = models.CharField(max_length=20, default="final")

    class Meta:
        unique_together = ("student","course","exam_type")

    def __str__(self):
        return f"{self.student} - {self.course} - {self.marks_obtained}/{self.max_marks}"
    