from django.contrib import admin
from .models import UserProfile  # Import only valid models
from .models import * # Import the Event and Program models
# Register your models here
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')  # Fields to display in the admin list view
    search_fields = ('user__username', 'phone_number')  # Fields to search
    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time')

@admin.register(Biblestudy)
class BiblestudyAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time')

@admin.register(Youth)
class YouthAdmin(admin.ModelAdmin):
    list_display = ['name']  # Ensure 'name' exists in the Youth model

@admin.register(Outreach)
class OutreachAdmin(admin.ModelAdmin):
    list_display = ['name']  # Ensure 'name' exists in the Outreach model
    
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('event', 'date', 'time')
                    
@admin.register(Roster)
class RosterAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'title',)
# Register the User model with the custom UserAdmin class

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'content')