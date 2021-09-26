from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, TemplateView, CreateView

from vacancies.forms import MyResumeForm
from vacancies.mixins import IsNotResumeMixin, IsResumeMixin
from vacancies.models import Resume


class MyResumeView(LoginRequiredMixin, IsNotResumeMixin, SuccessMessageMixin, UpdateView):
    model = Resume
    template_name = 'vacancies/resume/resume-edit.html'
    form_class = MyResumeForm
    login_url = 'login_page'
    success_message = 'Ваше резюме обновлено!'
    success_url = '/myresume/'

    def get_object(self):
        return self.model.objects.get(user_id=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(MyResumeView, self).get_context_data()
        context['head_title'] = 'Моe резюме | Джуманджи'
        return context


class NoResumeView(LoginRequiredMixin, TemplateView):
    template_name = 'vacancies/resume/resume-create.html'

    def get_context_data(self, **kwargs):
        context = super(NoResumeView, self).get_context_data()
        context['head_title'] = 'У вас нет резюме | Джуманджи'
        return context


class NewResumeCreateView(LoginRequiredMixin, IsResumeMixin, SuccessMessageMixin, CreateView):
    model = Resume
    template_name = 'vacancies/resume/resume-edit.html'
    form_class = MyResumeForm
    success_message = 'Резюме добавлено'
    success_url = '/myresume/'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.pk
        if form.is_valid():
            return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NewResumeCreateView, self).get_context_data()
        context['head_title'] = 'Создание резюме | Джуманджи'
        return context
