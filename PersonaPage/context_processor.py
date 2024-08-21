from django.shortcuts import get_object_or_404
from pages.models import Certification, Project, UserProfile

def project_context(request):
    if request.user.is_authenticated:
        # Try to get the UserProfile; if it doesn't exist, handle it gracefully
        user_profile = UserProfile.objects.filter(user=request.user).first()
        resume_url = user_profile.resume.url if user_profile and user_profile.resume else None
    else:
        user_profile = None
        resume_url = None

    context = {
        'me': user_profile,
        'certifications': Certification.objects.filter(is_visible=True),
        'portfolio': Project.objects.filter(is_displayed=True),
        'resume_url': resume_url,
    }
    return context
