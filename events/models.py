from django.db import models

# Create your models here.

class EventLocation(models.Model):
    name = models.CharField('Location Name', max_length=120)
    address = models.CharField(max_length=300, blank=True)
    zip_code = models.CharField('Zip Code', max_length=120, blank=True)


    def __str__(self):
        return self.name
    

class calUser(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField('User Email', blank=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName
    

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    event_location = models.ForeignKey(EventLocation, null=True, on_delete=models.CASCADE)
    #event_location = models.CharField(max_length=120)
    description = models.TextField(blank=False)
    attendees = models.ManyToManyField(calUser)

    def __str__(self):
        return self.name