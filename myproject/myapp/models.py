from django.db import models

# Create your models here.
class Feature:
    name: str
    details: str
    id: int
    is_true: bool

    def __init__(self, name, details, id):
        self.name = name
        self.details = details
        self.id = id
        self.is_true = bool(id%2)