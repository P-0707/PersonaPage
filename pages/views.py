from django.shortcuts import render, get_object_or_404, redirect
from pages.models import Certification, Project 
from django.contrib import messages 
from .forms import ContactForm
from django.utils.text import slugify

# View for the home page
def home(request):
    return render(request, 'core/home.html')


# View for the portfolio page
def projects(request):
    projects = Project.objects.all()  # Get all projects
    return render(request, 'core/projects.html', {'projects': projects})
    

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'core/project_detail.html', {'project': project})

def certification_detail(request, cert_id):
    certification = get_object_or_404(Certification, id=cert_id)
    return render(request, 'core/certification_details.html', {'certification': certification})

# View for the contact page
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the ContactEntry model instance
            messages.success(request, 'Thank you for reaching out. I have received your message and will be in touch shortly.')  # Add success message
            return redirect('pages:contact')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})



