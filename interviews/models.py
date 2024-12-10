from django.db import models

# Create your models here.
class InterviewQuestion(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    question = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class InterviewExperience(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.TextField()
    upvotes = models.PositiveIntegerField(default=0)

    

# /api/interviews/questions/
# /api/interviews/experiences/
