from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from django import forms
from tinymce.widgets import TinyMCE

from vacancies.models import Vacancy, Company, Application, Resume


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
            Row(
                Column('skills'),
            ),
            Row(
                Column('description'),
            ),

            FormActions(
                Submit('submit', 'Сохранить'),
            )
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
                Column('logo'),
            ),
            Row(
                Column('location'),
                Column('employee_count'),
            ),
            'description',
            FormActions(
                Submit('submit', 'Сохранить'),
            ),
        )


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'written_username',
            'written_phone',
            'written_cover_letter'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'written_username',
            'written_phone',
            'written_cover_letter',
            FormActions(
                Submit('submit', 'Отправить заявку'),
            ),
        )


class MyResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'name',
            'surname',
            'status',
            'salary',
            'specialty',
            'grade',
            'education',
            'experience',
            'portfolio',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('surname'),
            ),
            Row(
                Column('status'),
                Column('salary'),
            ),
            Row(
                Column('specialty'),
                Column('grade'),
            ),
            'education',
            'experience',
            'portfolio',
            FormActions(
                Submit('submit', 'Сохранить'),
            ),
        )
