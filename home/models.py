from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.forms.widgets import Textarea
from django.core.validators import MinValueValidator
from datetime import timedelta
from django.utils import timezone
import datetime

from django.conf import settings
# Create your models here.


class Team(models.Model):
    name=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)

class Game(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    team_1=ForeignKey(Team,blank=True,null=True,on_delete=CASCADE)

class SportLeage(models.Model):
    return None