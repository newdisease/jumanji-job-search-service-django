from django.db.models import Count
from django.views.generic import DetailView, TemplateView

from vacancies.models import Company, Vacancy


class CompanyDetailView(DetailView):
    template_name = 'vacancies/companies/company.html'
    context_object_name = 'company'
    queryset = Company.objects.annotate(count=Count('vacancies'))

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['available_vacancies'] = Vacancy.objects.filter(company=self.object).select_related('company')
        context['head_title'] = f'Джуманджи | Компания | {self.object.name}'
        return context


class MyCompany(TemplateView):
    template_name = 'vacancies/companies/company-edit.html'
