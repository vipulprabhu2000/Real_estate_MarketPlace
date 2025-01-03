from django.db import models
import uuid

# Create your models here.

class TimeStampUUIDModel(models.Model):
    pkid=models.BigAutoField(primary_key=True,editable=False)
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
