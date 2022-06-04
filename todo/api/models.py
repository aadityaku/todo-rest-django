from django.db import models

# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=200)
    status=models.BooleanField(default=True)
    obj=models.Manager()

    def __str__(self):
        return self.title


