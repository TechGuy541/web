from django.db import models
from django.utils import timezone

# Create your models here.
class GameEntry(models.Model):
    COMPATIBILITY_STATUS = [
        ('Perfect', 'Perfect'),
        ('Playable', 'Playable'),
        ('Menu', 'Menu'),
        ('Boots', 'Boots'),
        ('Nothing', 'Nothing'),
    ]

    RAM_CHOICES = [
        ('3GB', '3GB'),
        ('4GB', '4GB'),
        ('6GB', '6GB'),
        ('8GB', '8GB'),
        ('16GB', '16GB'),
    ]

    entry = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    game_id = models.CharField(max_length=100)
    description = models.TextField()
    compatibility = models.CharField(max_length=10, choices=COMPATIBILITY_STATUS)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    device_memory = models.CharField(max_length=4, choices=RAM_CHOICES)
    video = models.URLField(max_length=200, default="http://example.com/default-video")
    published = models.BooleanField(default=False)


