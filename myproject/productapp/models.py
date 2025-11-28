
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class CareerHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.TextField()
    interests = models.TextField()
    career_result = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'career_history'

    def __str__(self):
        return f"{self.user.username} - {self.career_result}"


