from django.urls import path
from django.conf import settings  # Add this import
from django.conf.urls.static import static
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),  # Updated to reflect the model name
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),  # Detail view for a single project
    path('contact/', views.contact_view, name='contact'),
    path('certification/<int:cert_id>/', views.certification_detail, name='certification_detail'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)