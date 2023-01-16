from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Plate(models.Model):
    _id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    createdAt = models.DateTimeField(
        'Дата cоздания', auto_now_add=True
    )

    def __str__(self):
        return f'{self.title}'

