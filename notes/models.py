from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=30000)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='notes')
    
