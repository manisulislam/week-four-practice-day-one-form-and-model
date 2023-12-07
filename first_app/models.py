from django.db import models

# Create your models here.
class myModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()