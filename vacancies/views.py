from django.db.models import Count
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from vacancies.models import Specialty, Company, Vacancy


class MainView(TemplateView):
    template_name = 'vacancies/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.annotate(
            count=Count('vacancies')
        )
        context['companies'] = Company.objects.annotate(
            count=Count('vacancies')
        )
        context['head_title'] = 'Джуманджи'
        return context


class VacanciesListView(ListView):
    template_name = 'vacancies/vacancies.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.all().select_related('company')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VacanciesListView, self).get_context_data(**kwargs)
        context['head_title'] = 'Джуманджи | Вакансии'
        context['page_title'] = 'Все вакансии'
        return context


class SelectedVacanciesListView(ListView):
    template_name = 'vacancies/vacancies.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        self.specialty = get_object_or_404(Specialty, code=self.args[0])
        return Vacancy.objects.filter(specialty_id=self.specialty.id).select_related('company')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SelectedVacanciesListView, self).get_context_data(**kwargs)
        context['head_title'] = f'Джуманджи | Вакансии | {self.specialty}'
        context['page_title'] = self.specialty
        return context


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        context = super(VacancyDetailView, self).get_context_data(**kwargs)
        context['head_title'] = f'Джуманджи | Вакансия | {self.object.title}'
        return context


class CompanyDetailView(DetailView):
    template_name = 'vacancies/company.html'
    context_object_name = 'company'
    queryset = Company.objects.annotate(count=Count('vacancies'))

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['available_vacancies'] = Vacancy.objects.filter(company=self.object).select_related('company')
        context['head_title'] = f'Джуманджи | Компания | {self.object.name}'
        return context


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
