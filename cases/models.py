from django.db import models

# Create your models here.

class case_table(models.Model):
    case_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.case_name}"