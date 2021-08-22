from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=50)
    date = models.DateTimeField()
    reminder = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.text[:10] + '...'