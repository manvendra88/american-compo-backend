from django.db import models

# Create your models here.
class active_law_table(models.Model):
    name = models.CharField(max_length=100)
    heading = models.CharField(max_length=50, null=True)
    card_image = models.ImageField(upload_to="active_lawsuits_images/")
    banner_image = models.ImageField(upload_to="active_lawsuits_images/")
    text = models.TextField(max_length=2000)