from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=12)
    location = models.CharField(max_length=20)
    logo = models.URLField(max_length=200, default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
    picture = models.URLField(max_length=200, default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
