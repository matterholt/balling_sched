from django.db import models


class Venue(models.Model):
    short_name = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.address} {self.city} {self.state} {self.zip_code}"
