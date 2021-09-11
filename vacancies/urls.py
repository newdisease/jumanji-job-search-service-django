from django.urls import path

from .views import MainListView, VacanciesListView

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
]
