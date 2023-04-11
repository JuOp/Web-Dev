from django.shortcuts import render
from django.http import JsonResponse
from hh_api.models import Company, Vacancy


def list_companies(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)


def get_company_by_id(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as exception:
        return JsonResponse({'exception': str(exception)}, status=400)
    return JsonResponse(company.to_json())


def list_vacancies_by_company(request, id):
    vacancies = Vacancy.objects.all().filter(company_id=id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def list_all_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def get_vacancy_by_id(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as exception:
        return JsonResponse({'exception': str(exception)}, status=400)
    return JsonResponse(vacancy.to_json())
    
def vacancies_top10(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

