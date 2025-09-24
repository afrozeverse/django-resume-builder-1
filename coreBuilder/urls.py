from django.urls import path
from . import views
urlpatterns = [
    path('resume-form/', views.resumeForm, name='resumeForm'),
    path('save-resume/', views.saveResume, name='saveResume'),
    path('my-resumes/', views.myResumes, name='myResumes'),
    path('edit-resume/<int:id>/', views.editResume, name='editResume'),
    path('delete-resume/<int:id>/', views.deleteResume, name='deleteResume'),
    path('download-resume/<int:id>/', views.downloadResume, name='downloadResume'),
    path('resume-templates/', views.resumeTemplates, name='resumeTemplates'),
]