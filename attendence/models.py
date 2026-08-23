from django.db import models
from students.models import Student
from courses.models import Course

class Attendence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendence_records")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="attendence_records")
    date = models.DateField()
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = ("student","course","date")
        #Doesn't create 2 rows for same student, same day , same course

    def __str__(self):
        status = "Present" if self.present else "Absent"
        return f"{self.student} - {self.date} - {status}" 