from django.db import models

class Item(models.Model):
    content = models.TextField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"item id:{self.pk}"