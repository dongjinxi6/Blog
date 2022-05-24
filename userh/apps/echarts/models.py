from django.db import models

# Create your models here.


class echarts_user(models.Model):
    ec_name = models.CharField(max_length=40)
    