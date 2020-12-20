from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=60)
    code = models.CharField(max_length=8)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name
