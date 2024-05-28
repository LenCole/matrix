import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.date_updated = timezone.now()
        super().save(*args, **kwargs)

class IsActiveModel(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class URLModel(models.Model):
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    class Meta:
        abstract = True
