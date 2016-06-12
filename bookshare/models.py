from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
	user = models.OneToOneField(User)
	extra = models.CharField(max_length = 200, default = "Test")
# Create your models here.
