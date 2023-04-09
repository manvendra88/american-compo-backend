from django.db import models

class contact_us_table(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)