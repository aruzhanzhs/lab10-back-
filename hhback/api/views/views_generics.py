from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from hhback.api.models import Company, Vacancy
from hhback.api.serializers import CompanySerializer2, VacancySerializer


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2
    permission_classes = (IsAuthenticated,)


class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2


class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class CompanyWithVacancyAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyWithVacancySerializer
