from django.db import models


class Users(models.Model):
    id = models.CharField(max_length=10, default=0, primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Reports(models.Model):
    num = models.CharField(max_length=10, default=0, primary_key=True)
    year = models.CharField(max_length=4)
    text = models.CharField(max_length=500)
