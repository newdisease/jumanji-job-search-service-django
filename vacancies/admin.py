from django.contrib import admin

from .models import Company, Specialty, Vacancy


class Companies(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'employee_count',
        'owner',
    )


class Specialities(admin.ModelAdmin):
    pass


class Vacancies(admin.ModelAdmin):
    list_display = (
        'title',
        'specialty',
        'company',
        'published_at',
    )


admin.site.register(Company, Companies)
admin.site.register(Specialty, Specialities)
admin.site.register(Vacancy, Vacancies)
