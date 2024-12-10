from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=[('applied', 'Applied'), ('interview', 'Interview'), ('rejected', 'Rejected')])


# /api/jobs/
# /api/jobs/{id}/apply/
# /api/jobs/{id}/save/