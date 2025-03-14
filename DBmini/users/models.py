from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Technical','Technical'),
        ('Non Technical', 'Non Technical'),
        ('Sports', 'Sports'),
        ('Gaming', 'Gaming')
    ]

    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='event_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.name}"