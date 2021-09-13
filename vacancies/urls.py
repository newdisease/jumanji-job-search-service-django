from django.urls import path, re_path

from .views import MainView, VacanciesListView, SelectedVacanciesListView, VacancyDetailView, CompanyDetailView

urlpatterns = [
    path('', MainView.as_view(), name='main_view'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies_view'),
    re_path(r'^vacancies/cat/([\w-]+)/$', SelectedVacanciesListView.as_view()),
    path('vacancies/<int:pk>', VacancyDetailView.as_view(), name='vacancy_view'),
    path('companies/<int:pk>', CompanyDetailView.as_view(), name='company_view'),
]
