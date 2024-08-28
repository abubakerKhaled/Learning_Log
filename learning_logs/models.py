from django.db import models
from django.utils import timezone

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        """Returns a string representation of the model."""
        return self.text