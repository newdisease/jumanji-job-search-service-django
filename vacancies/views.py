from django.views.generic import TemplateView


class MainListView(TemplateView):
    template_name = 'vacancies/index.html'


class VacanciesListView(TemplateView):
    template_name = 'vacancies/vacancies.html'

