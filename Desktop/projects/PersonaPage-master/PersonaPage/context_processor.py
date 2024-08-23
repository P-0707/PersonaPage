from django.shortcuts import get_object_or_404
from pages.models import Certification, Project, UserProfile
from django.contrib.auth.models import User

def project_context(request):
    try:
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.filter(user=request.user).first()
        else:
            default_user = User.objects.get(username='root')
            user_profile = UserProfile.objects.filter(user=default_user).first()
    except User.DoesNotExist:
        user_profile = None

    resume_url = user_profile.resume.url if user_profile and user_profile.resume else None

    context = {
        'me': user_profile,
        'certifications': Certification.objects.filter(is_visible=True),
        'portfolio': Project.objects.filter(is_displayed=True),
        'resume_url': resume_url,
    }
    return context

