from django.db import models

class Company(models.Model):
    number = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    linkedin_url = models.URLField(blank=True, null=True)
    current_employee_estimate = models.IntegerField(default=0)
    total_employee_estimate = models.IntegerField()

    def __str__(self):
        return self.name
