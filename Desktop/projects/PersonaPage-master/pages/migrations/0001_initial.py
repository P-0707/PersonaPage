# Generated by Django 4.2.14 on 2024-08-19 12:21

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awarded_date', models.DateTimeField(blank=True, null=True)),
                ('issuing_organization', models.CharField(max_length=50)),
                ('certification_title', models.CharField(blank=True, max_length=200, null=True)),
                ('certification_description', models.CharField(blank=True, max_length=500, null=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Certification',
                'verbose_name_plural': 'Certifications',
                'ordering': ['-awarded_date'],
            },
        ),
        migrations.CreateModel(
            name='ContactEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('sender_name', models.CharField(max_length=100, verbose_name='Name')),
                ('sender_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message_content', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact Entry',
                'verbose_name_plural': 'Contact Entries',
                'ordering': ['-submitted_at'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('project_name', models.CharField(max_length=200)),
                ('short_description', models.CharField(blank=True, max_length=500, null=True)),
                ('detailed_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='portfolio')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('is_displayed', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('proficiency', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('expert', 'Expert')], default='beginner', max_length=12)),
                ('icon', models.FileField(blank=True, null=True, upload_to='skills')),
                ('is_primary', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='avatar')),
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='cv')),
                ('skills', models.ManyToManyField(blank=True, to='pages.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]