from django.db import models

# Create your models here.
class Task(models.Model):
    assignment = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    classes = models.CharField(max_length=100)
    duedate = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.assignment

    def __tuple__(self):
        return self.assignment, self.type, self.classes, self.duedate