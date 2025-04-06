from django.db import models

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)

    def __str__(self):
        # Ensure this returns a string, not a tuple
        return f"{self.field1} - {self.field2}"  # Example string representation
