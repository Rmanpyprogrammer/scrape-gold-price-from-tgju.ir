from django.db import models


class Price_online(models.Model):
    value=models.IntegerField(default=0)
    date=models.DateTimeField(null=True, blank=True)
