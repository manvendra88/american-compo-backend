from django.db import models

# Create your models here.
class about_us_table(models.Model):
    image = models.ImageField()
    text = models.TextField(max_length=5000)