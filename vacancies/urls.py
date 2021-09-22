from django.urls import path, re_path

from .views import MainView, VacanciesListView, SelectedVacanciesListView, VacancyDetailView, CompanyDetailView, \
    MyCompany, MyCompanyVacancies, NewCompanyCreate, NoCompany

urlpatterns = [
    path('', MainView.as_view(), name='main_view'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies_view'),
    re_path(r'^vacancies/cat/([\w-]+)/$', SelectedVacanciesListView.as_view(), name='selected_vacancies_view'),
    path('vacancies/<int:pk>', VacancyDetailView.as_view(), name='vacancy_view'),
    path('companies/<int:pk>', CompanyDetailView.as_view(), name='company_view'),
    # личный кабинет
    path('mycompany/', MyCompany.as_view(), name='my_company'),
    path('mycompany/letsstart/', NoCompany.as_view(), name='no_company'),
    path('mycompany/create/', NewCompanyCreate.as_view(), name='new_company_create'),
    path('mycompany/vacancies/', MyCompanyVacancies.as_view(), name='my_company_vacancies'),
    #path('mycompany/vacancies/1', MyCompanyVacancy.as_view(), name='my_company_vacancy'),

]
