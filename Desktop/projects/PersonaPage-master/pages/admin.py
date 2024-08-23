from django.contrib import admin
from .models import Skill, UserProfile, ContactEntry, Project, Certification

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):  # Fixed class name and inheritance
    list_display = ('name', 'proficiency', 'is_primary')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'job_title', 'biography')
    fields = ('user', 'profile_picture', 'job_title', 'biography', 'skills', 'resume', 'first_name', 'last_name')

@admin.register(ContactEntry)
class ContactEntryAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'submitted_at')
    ordering = ['-submitted_at']
    search_fields = ('sender_name', 'sender_email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'published_date', 'is_displayed')
    prepopulated_fields = {'slug': ('project_name',)}

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('certification_title', 'issuing_organization', 'awarded_date', 'is_visible')
    fields = ('certification_title', 'issuing_organization', 'awarded_date', 'certification_description', 'certification_image', 'is_visible')
    search_fields = ('certification_title', 'issuing_organization')
    list_filter = ('is_visible', 'awarded_date')
    fields = ('certification_title', 'certification_description', 'certification_image', 'issuing_organization', 'awarded_date', 'is_visible')
    readonly_fields = ('awarded_date',)
