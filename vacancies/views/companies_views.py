from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView

from vacancies.forms import MyCompanyForm, MyCompanyVacancyForm
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


class NoCompanyView(LoginRequiredMixin, IsCompanyMixin, TemplateView):
    template_name = 'vacancies/companies/company-create.html'


class NewCompanyCreateView(LoginRequiredMixin, IsCompanyMixin, SuccessMessageMixin, CreateView):
    model = Company
    template_name = 'vacancies/companies/company-edit.html'
    form_class = MyCompanyForm
    success_message = 'Компания добавлена'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MyCompanyView(LoginRequiredMixin, IsNotCompanyMixin, SuccessMessageMixin, UpdateView):
    model = Company
    template_name = 'vacancies/companies/company-edit.html'
    form_class = MyCompanyForm
    login_url = 'login_page'
    success_message = 'Информация о компании обновлена'

    def get_object(self):
        return self.model.objects.get(owner_id=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(MyCompanyView, self).get_context_data()
        context['head_title'] = 'Джуманджи | Моя компания'
        return context


class MyCompanyVacanciesView(LoginRequiredMixin, IsNotCompanyMixin, ListView):
    template_name = 'vacancies/vacancy-list.html'
    context_object_name = 'my_company_vacancies'
    login_url = 'login_page'

    def get_queryset(self):
        username = self.request.user.username
        return Vacancy.objects.filter(company__owner__username=username)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MyCompanyVacanciesView, self).get_context_data()
        context['head_title'] = 'Джуманджи | Мои вакансии'
        context['page_title'] = 'Все мои вакансии'
        return context


class MyCompanyVacancyView(LoginRequiredMixin, IsNotCompanyMixin, SuccessMessageMixin, UpdateView):
    template_name = 'vacancies/vacancy-edit.html'
    form_class = MyCompanyVacancyForm
    login_url = 'login_page'
    success_message = "Вакансия обновлена"

    def get_queryset(self):
        username = self.request.user.username
        return Vacancy.objects.filter(company__owner__username=username)

    def get_context_data(self, **kwargs):
        context = super(MyCompanyVacancyView, self).get_context_data()
        context['head_title'] = f'Джуманджи | Вакансия | {self.object.title}'
        return context

    def get_success_url(self):
        return reverse_lazy('my_company_vacancy', args=(self.object.pk,))
