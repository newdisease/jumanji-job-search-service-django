from django.db.models import Count
from django.views.generic import TemplateView, ListView, DetailView

from vacancies.models import Specialty, Company, Vacancy


class MainView(TemplateView):
    template_name = 'vacancies/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.annotate(count=Count('vacancies'))
        context['companies'] = Company.objects.annotate(count=Count('vacancies'))
        context['head_title'] = 'Джуманджи'
        return context


class VacanciesListView(ListView):
    template_name = 'vacancies/vacancies.html'
    model = Vacancy
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VacanciesListView, self).get_context_data(**kwargs)
        context['head_title'] = 'Джуманджи | Вакансии'
        context['page_title'] = 'Все вакансии'
        return context


class SelectedVacanciesListView(ListView):
    template_name = 'vacancies/vacancies.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        specialty_id = Specialty.objects.get(code=self.args[0]).id
        return Vacancy.objects.filter(specialty_id=specialty_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SelectedVacanciesListView, self).get_context_data(**kwargs)
        context['page_title'] = Specialty.objects.get(code=self.args[0]).title
        return context


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        context = super(VacancyDetailView, self).get_context_data(**kwargs)
        context['specialties_code'] = Specialty.objects.get(id=self.object.specialty_id).code
        context['head_title'] = f'Джуманджи | Вакансия | {Vacancy.objects.get(id=self.object.id).title}'
        return context


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'vacancies/company.html'
    context_object_name = 'company'
    queryset = Company.objects.annotate(count=Count('vacancies'))

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['available_vacancies'] = Vacancy.objects.filter(company=self.object)
        context['head_title'] = f'Джуманджи | Компания | {Company.objects.get(name=self.object.name).name}'
        return context
