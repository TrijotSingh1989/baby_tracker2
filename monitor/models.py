from django.db import models

class Event(models.Model):
    EVENT_CHOICES = [
        ('sleep', 'Sleep'),
        ('feed', 'Feed'),
        ('poop', 'Poop'),
        ('diaper_change', 'Diaper Change'),
    ]
    
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    event_time = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True, blank=True)  # Optional duration for event
    
    def __str__(self):
        return f"{self.event_type.capitalize()} at {self.event_time.strftime('%Y-%m-%d %H:%M:%S')}"
