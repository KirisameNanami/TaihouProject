# coding:utf-8
from django.db import models

# Create your models here.
class Account(models.Model):
    AccountName = models.CharField(u'Account',max_length=256)
    RegisterTime=models.DateTimeField(u'RegisterTime',auto_now_add=True,editable=True)
    LoginAuth=models.BooleanField(default=False)
    def __unicode__(self):
        return self.AccountName
    def __str__(self):
        return self.AccountName
