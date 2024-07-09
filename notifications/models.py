from django.db import models
import uuid

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payload = models.JSONField()
    type = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    message =  models.CharField(max_length=300)

    def __str__(self):
        return f'Notification - {self.type}'
