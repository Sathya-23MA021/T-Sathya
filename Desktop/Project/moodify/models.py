from django.db import models
from django.contrib.auth.models import User

class MoodTracker(models.Model):
    name = models.CharField(max_length=50)
    # date = models.DateField()
    # time = models.TimeField()
    mood = models.CharField(max_length=50)  
    mood_intensity = models.IntegerField()  # Mood intensity (1-10)
    performance = models.CharField(max_length=50) 
    performance_score = models.IntegerField()  # Optional performance score (1-10)
    stress_level = models.CharField(max_length=50) 
    energy_level = models.CharField(max_length=50) 
    physical_health = models.TextField()  
    activities = models.TextField()  
    social_interaction = models.TextField()  
    weather = models.CharField(max_length=50)  
    mental_clarity = models.CharField(max_length=50)  
    gratitude_notes = models.TextField()  
    self_care = models.TextField()  

    def __str__(self):
        return "{self.user.username} - {self.date} - {self.mood}"