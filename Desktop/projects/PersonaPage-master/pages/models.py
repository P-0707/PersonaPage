from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Model for representing the user's skills.
class Skill(models.Model):
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    PROFICIENCY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    name = models.CharField(max_length=40)
    proficiency = models.CharField(max_length=12, choices=PROFICIENCY_LEVELS, default='beginner')
    icon = models.FileField(blank=True, null=True, upload_to="skills")
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    
# Model for storing the user's profile information.
class UserProfile(models.Model):
    class Meta:
        verbose_name = 'User Profile'  # Singular name used in admin and forms
        verbose_name_plural = 'User Profiles'  # Plural name used in admin and forms

    first_name = models.CharField(max_length=30, blank=True, null=True)  # Add this field
    last_name = models.CharField(max_length=30, blank=True, null=True) 
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the Django User model
    profile_picture = models.ImageField(blank=True, null=True, upload_to='avatar')  # Profile picture of the user
    job_title = models.CharField(max_length=200, blank=True, null=True)  # User's professional title (e.g., Software Engineer)
    biography = models.TextField(blank=True, null=True)  # Short bio or introduction about the user
    skills = models.ManyToManyField(Skill, blank=True)  # Skills associated with this user profile
    resume = models.FileField(blank=True, null=True, upload_to='cv')  # File upload for the user's CV or resume

    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else f'{self.user.username}'
    
# Model for storing contact form submissions from the website.
class ContactEntry(models.Model):
    class Meta:
        verbose_name = 'Contact Entry'  # Singular name used in admin and forms
        verbose_name_plural = 'Contact Entries'  # Plural name used in admin and forms
        ordering = ["-submitted_at"]  # Order by submission date, newest first

    submitted_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the contact form is submitted
    sender_name = models.CharField(verbose_name="Name", max_length=100)  # Name of the person submitting the form
    sender_email = models.EmailField(verbose_name="Email")  # Email of the person submitting the form
    message_content = models.TextField(verbose_name="Message")  # Message sent by the user

    def __str__(self):
        return f'{self.sender_name} ({self.sender_email})'  # Display sender's name and email in admin or when printed
    
# Model for showcasing the user's projects or portfolio items.
class Project(models.Model):
    class Meta:
        verbose_name = 'Project'  # Singular name used in admin and forms
        verbose_name_plural = 'Projects'  # Plural name used in admin and forms
        ordering = ["-published_date"]  # Order by publication date, newest first

    published_date = models.DateTimeField(blank=True, null=True)  # Date when the project was completed or published
    project_name = models.CharField(max_length=200)  # Name of the project
    short_description = models.CharField(max_length=500, blank=True, null=True)  # Brief description of the project
    detailed_description = RichTextField(blank=True, null=True)  # Full details about the project
    cover_image = models.ImageField(blank=True, null=True, upload_to="portfolio")  # Image or screenshot of the project
    slug = models.SlugField(null=True, blank=True)  # URL-friendly version of the project name
    is_displayed = models.BooleanField(default=True)  # Whether the project should be shown on the website

    def save(self, *args, **kwargs):
        if not self.slug:  # Automatically generate slug if not provided
            self.slug = slugify(self.project_name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.project_name  # Display project name in admin or when printed

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"  # URL path for viewing this project on the website



class Certification(models.Model):
    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'
        ordering = ["-awarded_date"]

    awarded_date = models.DateTimeField(blank=True, null=True)
    issuing_organization = models.CharField(max_length=50)
    certification_title = models.CharField(max_length=200, blank=True, null=True)
    certification_description = RichTextField(blank=True, null=True)
    certification_image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.certification_title or "No Title"  # Display certification title in admin or when printed
