from django.db import models

# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    is_ready_to_eat = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
