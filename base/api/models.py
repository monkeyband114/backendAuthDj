from typing import Any
from django.db import models
from django.contrib.auth.models import User


class Blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(blank=False, null=False, max_length=500)
    text = models.CharField(blank=False, null=False, max_length=500)
    # image
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        return self.title







