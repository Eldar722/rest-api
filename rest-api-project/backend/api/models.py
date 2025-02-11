from django.db import models
from datetime import datetime

class Item(models.Model):
    content = models.TextField()
    is_finished = models.BooleanField(default=False)
    created_At = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"item id:{self.pk}"