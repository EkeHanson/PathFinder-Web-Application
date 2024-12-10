from django.db import models
from users.models import User

# Create your models here.
class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)


# /api/mentorship/mentors/
# /api/mentorship/requests/