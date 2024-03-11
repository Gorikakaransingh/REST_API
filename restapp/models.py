from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cleint(models.Model):
    client = models.CharField(max_length = 20)
    branch = models.CharField(max_length = 10)
    user = models.OneToOneRel(User)

