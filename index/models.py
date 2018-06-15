from django.db import models


class Users(models.Model):
    class Meta():
        verbose_name = '用户'
        verbose_name_plural = '所有用户'
    id = models.CharField(max_length=10, default=0, primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.id, self.name, self.password


class Reports(models.Model):
    class Meta():
        verbose_name = '年报'
        verbose_name_plural = '所有年报'
    num = models.CharField(max_length=10, default=0, primary_key=True)
    year = models.CharField(max_length=4)
    text = models.TextField()

    def __unicode__(self):
        return self.num, self.year, self.text
