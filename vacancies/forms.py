from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Field
from django import forms
from tinymce.widgets import TinyMCE

from vacancies.models import Vacancy, Company


class CustomImagefield(Field):
    template = 'custom_imagefield.html'


class MyCompanyVacancyForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Vacancy
        fields = [
            'title',
            'specialty',
            'skills',
            'description',
            'salary_min',
            'salary_max',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title'),
                Column('specialty')
            ),
            Row(
                Column('salary_min'),
                Column('salary_max')
            ),
            'skills',
            'description',
            FormActions('submit', 'Сохранить')
        )


class MyCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'logo',
            'location',
            'employee_count',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column(CustomImagefield('logo')),
            ),
            Row(
                Column('location'),
                Column('employee_count'),
            ),
            'description',
            FormActions(
                Submit('submit', 'Сохранить')
            )
        )
