from django.urls import path
#from rest_framework_jwt.views import obtain_jwt_token

#version 1
from hhback.api.views.views_v1 import companies_list, company_detail, company_vacancies, vacancies, vacancy, vacancies_top

#class based view
from hhback.api.views.views_cbv import CompanyListAPIView, CompanyDetailAPIView, CompanyWithVacancyListAPIView, \
    VacancyListAPIView, VacancyDetailAPIView

urlpatterns = [

    #cbv
    # path('companies/', CompanyListAPIView.as_view()),
    # path('companies/<int:company_id>', CompanyDetailAPIView.as_view()),
    # path('companies/<int:company_id>/vacancies/', CompanyWithVacancyListAPIView.as_view()),
    # path('vacancies/', VacancyListAPIView.as_view()),
    # path('vacancies/<int:vacancy_id>', VacancyDetailAPIView.as_view()),

    #version 1
    path('companies/', companies_list),
    path('companies/<int:id>/', company_detail),
    path('companies/<int:id>/vacancies/', company_vacancies),
    path('vacancies/', vacancies),
    path('vacancies/<int:id>/', vacancy),
    path('vacancies/top_ten/', vacancies_top),
    #path('login/', obtain_jwt_token)
]