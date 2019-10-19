from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import validate_email
import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    timer = models.IntegerField(default=0)
    email_1 = models.EmailField(max_length=20, validators=[
                                validate_email], default="player_1@gmail.com", editable=True)
    email_2 = models.EmailField(max_length=20, validators=[
                                validate_email], default="player_2@gmail.com", editable=True, blank=True)
    email_3 = models.EmailField(max_length=20, validators=[
                                validate_email], default="player_3@gmail.com", editable=True, blank=True)
    name_1 = models.CharField(max_length=20, default="player_1", editable=True)
    name_2 = models.CharField(
        max_length=20, default="player_2", editable=True, blank=True)
    name_3 = models.CharField(
        max_length=20, default="player_3", editable=True, blank=True)
    number_1 = models.CharField(max_length=12, editable=True)
    number_2 = models.CharField(max_length=12, editable=True, blank=True)
    number_3 = models.CharField(max_length=12, editable=True, blank=True)
    add_time = models.IntegerField(default=0)
    sel_ques = models.CharField(max_length=200)
    ansq = models.CharField(max_length=100, default="")


class MCQ(models.Model):
    question = models.TextField(max_length=500, default=' ')
    answer = models.IntegerField(default=' ')
    A = models.TextField(max_length=150, default=' ')
    B = models.TextField(max_length=150, default=' ')
    C = models.TextField(max_length=150, default=' ')
    D = models.TextField(max_length=150, default=' ')
    img = models.FileField(blank=True, null=True)
