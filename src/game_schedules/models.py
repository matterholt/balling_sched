from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.description}'

class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.address} {self.city} {self.state} {self.zip_code}'

class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    field = models.CharField(max_length=200)
    home = models.CharField(max_length=200)
    visitor = models.CharField(max_length=200)

    location = models.ForeignKey(Venue, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return f'å{self.date} {self.time}'
