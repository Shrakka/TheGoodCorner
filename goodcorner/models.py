from django.db import models
import uuid

class User(models.Model):
    surname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.surname

class Announce(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    creation_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hashurl = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title