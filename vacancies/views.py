from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'vacancies/index.html'


class VacanciesListView(TemplateView):
    template_name = 'vacancies/vacancies.html'


class GroupedVacanciesListView(TemplateView):
    template_name = 'vacancies/vacancies.html'


class CompanyView(TemplateView):
    template_name = 'vacancies/company.html'


class VacancyView(TemplateView):
    template_name = 'vacancies/vacancy.html'
