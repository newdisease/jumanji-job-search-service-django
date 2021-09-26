from django.db.models import Count
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormMixin

from vacancies.forms import ApplicationForm
from vacancies.mixins import IsSendApplicationMixin
from vacancies.models import Specialty, Company, Vacancy


class MainView(TemplateView):
    template_name = 'index.html'

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
        context['head_title'] = 'Вакансии | Джуманджи'
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
        context['head_title'] = f'{self.specialty} | Джуманджи | Вакансии'
        context['page_title'] = self.specialty
        return context


class VacancyDetailView(FormMixin, DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'
    context_object_name = 'vacancy'
    form_class = ApplicationForm


    def get_context_data(self, **kwargs):
        context = super(VacancyDetailView, self).get_context_data(**kwargs)
        context['head_title'] = f'{self.object.title} | Вакансия | Джуманджи'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.vacancy_id = self.object.pk
        form.save()
        return super(VacancyDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('vacancy_response_send', args=(self.object.pk,))


class VacancyResponseView(IsSendApplicationMixin, DetailView):
    template_name = 'vacancies/resume/sent.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(VacancyResponseView, self).get_context_data(**kwargs)
        context['head_title'] = 'Отклик отправлен | Джуманджи'
        context['vacancy_id'] = self.object
        return context


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
