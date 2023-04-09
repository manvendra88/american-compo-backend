from django.db import models

# Create your models here.
class active_lawsuit_table(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="active_lawsuits_images/")
    text = models.TextField(max_length=2000)