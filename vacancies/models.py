from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from config.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    logo = models.ImageField(
        upload_to=MEDIA_COMPANY_IMAGE_DIR,
        blank=True
    )
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('my_company')


class Specialty(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
    picture = models.ImageField(
        upload_to=MEDIA_SPECIALITY_IMAGE_DIR,
        blank=True
    )

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
        related_name="vacancies"
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="vacancies"
    )
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=50)
    written_phone = models.CharField(max_length=12)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    def __str__(self):
        return self.written_username


class Resume(models.Model):
    class Status(models.TextChoices):
        NOT_LOOKING_FOR = 'Не ищу работу'
        CHECK = 'Рассматриваю предложения'
        LOOKING_FOR = 'Ищу работу'

    class Grade(models.TextChoices):
        TRAINEE = 'Стажер'
        JUNIOR = 'Джуниор'
        MIDDLE = 'Миддл'
        SENIOR = 'Синьор'
        LEAD = 'Лид'

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    status = models.CharField(
        max_length=24,
        choices=Status.choices,
        default=Status.CHECK
    )
    salary = models.IntegerField()
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
        related_name='resume'
    )
    grade = models.CharField(
        max_length=10,
        choices=Grade.choices,
        default=Grade.JUNIOR
    )
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.URLField()

    def __str__(self):
        return f'{self.name} {self.surname}'
