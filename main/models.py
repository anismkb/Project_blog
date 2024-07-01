from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Blog (models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField(default=timezone.localdate)

    def __str__(self):
        return self.title