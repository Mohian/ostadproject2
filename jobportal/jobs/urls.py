from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name='home'),
    path('jobs/', views.JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('jobs/create/', views.JobCreateView.as_view(), name='job_create'),
    path('jobs/<int:pk>/apply/', views.ApplicationCreateView.as_view(), name='application_create'),
    path('employer/dashboard/', views.EmployerJobListView.as_view(), name='employer_dashboard'),
    path('employer/jobs/<int:pk>/applications/', views.JobApplicationsView.as_view(), name='job_applications'),
    path('applicant/dashboard/', views.ApplicantApplicationListView.as_view(), name='applicant_dashboard'),
]