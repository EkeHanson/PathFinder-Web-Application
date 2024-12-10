from django.db import models

# Create your models here.
class User(AbstractUser):
    is_recruiter = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    resume = models.FileField(upload_to="resumes/", blank=True)


#     /api/users/register/
# /api/users/login/
# /api/users/profile/
