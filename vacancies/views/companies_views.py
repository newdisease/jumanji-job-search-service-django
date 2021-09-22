from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView

from vacancies.forms import MyCompanyForm
from vacancies.mixins import IsNotCompanyMixin, IsCompanyMixin
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


class NoCompany(LoginRequiredMixin, IsCompanyMixin, TemplateView):
    template_name = 'vacancies/companies/company-create.html'


class NewCompanyCreate(LoginRequiredMixin, IsCompanyMixin, CreateView):
    model = Company
    template_name = 'vacancies/companies/company-edit.html'
    form_class = MyCompanyForm
    login_url = 'login_page'
    success_url = '/mycompany/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MyCompany(LoginRequiredMixin, IsNotCompanyMixin, UpdateView):
    model = Company
    template_name = 'vacancies/companies/company-edit.html'
    form_class = MyCompanyForm
    login_url = 'login_page'

    def get_object(self):
        return self.model.objects.get(owner_id=self.request.user.pk)


class MyCompanyVacancies(LoginRequiredMixin, ListView):
    template_name = 'vacancies/vacancy-list.html'
    context_object_name = 'my_company_vacancies'
    login_url = 'login_page'

    def get_queryset(self):
        username = self.request.user.username
        return Vacancy.objects.filter(company__owner__username=username)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MyCompanyVacancies, self).get_context_data()
        context['head_title'] = 'Джуманджи | Мои вакансии'
        context['page_title'] = 'Все мои вакансии'
        return context

# class MyCompanyVacancy(View):
#     vacancy = get_object_or_404(Vacancy, pk=1)
#     vacancy_form = MyCompanyVacancyForm(request.POST)
#     if vacancy_form.is_valid():
#         vacancy = vacancy_form.save(commit=False)
#         vacancy.title = vacancy.title
#         vacancy.company = vacancy.company
#         vacancy.save()
