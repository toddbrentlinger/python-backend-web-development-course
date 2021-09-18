from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

    # def __init__(self, name, details, id):
    #     self.name = name
    #     self.details = details
    #     self.id = id
    #     self.is_true = bool(id%2)