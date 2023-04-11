from django.urls import path
from hh_api.views import list_companies, get_company_by_id, list_vacancies_by_company, list_all_vacancies, get_vacancy_by_id, vacancies_top10

urlpatterns = [
    path('companies', list_companies),
    path('companies/<int:id>/', get_company_by_id),
    path('companies/<int:id>/vacancies/', list_vacancies_by_company),
    path('vacancies/', list_all_vacancies),
    path('vacancies/<int:id>/', get_vacancy_by_id),
    path('vacancies/top_ten/', vacancies_top10),
]