from django.urls import path

from .views import MainView, VacanciesListView, GroupedVacanciesListView, CompanyView, VacancyView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
    path('vacancies/cat/frontend', GroupedVacanciesListView.as_view(), name='grouped_vacancies'),
    path('companies/345', CompanyView.as_view(), name='company'),
    path('vacancies/22', VacancyView.as_view(), name='vacancy'),
]
