from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_EMPLOYER = 'employer'
    ROLE_APPLICANT = 'applicant'
    ROLE_CHOICES = [
        (ROLE_EMPLOYER, 'Employer'),
        (ROLE_APPLICANT, 'Applicant'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)