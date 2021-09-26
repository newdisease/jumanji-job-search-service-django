from django.urls import path, re_path

from .views import MainView, VacanciesListView, SelectedVacanciesListView, VacancyDetailView, CompanyDetailView, \
    MyCompanyView, MyCompanyVacanciesView, NewCompanyCreateView, NoCompanyView, MyCompanyVacancyView, \
    VacancyResponseView, MyNewVacancyView

urlpatterns = [
    path('', MainView.as_view(), name='main_view'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies_view'),
    re_path(r'^vacancies/cat/([\w-]+)/$', SelectedVacanciesListView.as_view(), name='selected_vacancies_view'),
    path('vacancies/<int:pk>', VacancyDetailView.as_view(), name='vacancy_view'),
    path('vacancies/<int:pk>/send/', VacancyResponseView.as_view(), name='vacancy_response_send'),
    path('companies/<int:pk>', CompanyDetailView.as_view(), name='company_view'),
    # личный кабинет
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/letsstart/', NoCompanyView.as_view(), name='no_company'),
    path('mycompany/create/', NewCompanyCreateView.as_view(), name='new_company_create'),
    path('mycompany/vacancies/', MyCompanyVacanciesView.as_view(), name='my_company_vacancies'),
    path('mycompany/vacancies/<int:pk>', MyCompanyVacancyView.as_view(), name='my_company_vacancy'),
    path('mycompany/vacancies/new/', MyNewVacancyView.as_view(), name='my_new_vacancy'),

]
