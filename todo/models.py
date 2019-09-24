from django.db import models
from django.conf import settings


# Create your models here.

class Todo(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="cascade")
    text = models.CharField(max_length=500, blank=False, null=False)
    due_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.text
