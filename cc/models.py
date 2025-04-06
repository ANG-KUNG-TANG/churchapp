from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one field  
    
    def __str__(self):
        return self.user.username  
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)   
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # save the profile of the user

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Schedule(models.Model):
    event = models.CharField(max_length=100)
    date = models.DateTimeField()
    pastor = models.CharField(max_length=100, default="Unknown Pastor")  # Added default value
    time = models.CharField(max_length=200, default="00:00")  # Added time field
    def __str__(self):
        return f"Title{self.event}  Date {self.date.strftime('%Y-%m-%d %H:%M:%S')} Time{self.time} Pastor{self.pastor}"
    
class Roster(models.Model):
    name = models.CharField(max_length=100)
    role = models.DateTimeField()
    title= models.CharField(max_length=200)
    def __str__(self):
        return f"Name{self.name} - Role{self.role} - Title{self.title}"

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    pastor = models.CharField(max_length=100, default="Unknown Pastor")  # Added default value 
    time = models.CharField(max_length=200, default="00:00")  # Added time field
    def __str__(self):
        return f"Title{self.name} Date{self.date.astimezone().strftime('%Y-%m-%d %H:%M:%S')} Time{self.time} Pastor{self.pastor}"
    
class Biblestudy(models.Model):  # Ensure the name matches the imports
    name = models.CharField(max_length=100) 
    date = models.DateTimeField()
    time = models.CharField(max_length=200)  # Added time field
    leader = models.CharField(max_length=100, default="Unknown Leader")  # Added default value
    def __str__(self):
        date_str = self.date.strftime('%Y-%m-%d %H:%M:%S') if self.date else "No Date"
        return f"Bible Study{self.name}  {date_str} at {self.time}"

class Youth(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=255)  # Add this if it doesn't exist
    leader = models.CharField(max_length=100, default="Unknown Leader")  # Added default value
    time = models.CharField(max_length=200)  # Added time field
    def __str__(self):
        return f"Title{self.name} Date{self.date.strftime('%Y-%m-%d %H:%M:%S')} Tme{self.time} Leader{self.leader}"

class Outreach(models.Model):
    date = models.DateTimeField()
    time = models.CharField(max_length=200)
    location = models.CharField(max_length=100, default="Unknown Location")  # Added default value
    name = models.CharField(max_length=255)  # Add this if it doesn't exist
    def __str__(self):
        return f"Title{self.name} Time{self.date.strftime('%Y-%m-%d %H:%M:%S')} Time{self.time} Location{self.location}"
    
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the announcement is created
    author = models.CharField(max_length=100, default="Unknown Author")  # Added default value
    def __str__(self):
        return self.title

