from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
	user = models.OneToOneField(User)
	first_time = models.BooleanField(default = False)
	
# Create your models here.
