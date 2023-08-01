from django.db import models
from django.urls import reverse,resolve

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("advanced:school_detail",kwargs={'pk':self.pk})

    def get_student_len(self):
        return self.students

class Student(models.Model):
    name = models.CharField(max_length=264)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("advanced:school_detail",kwargs={'pk':self.school.pk})
