from django.db import models


class Contributor(models.Model):
    name = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    graduation = models.DateField()

    def __str__(self):
        return self.name


