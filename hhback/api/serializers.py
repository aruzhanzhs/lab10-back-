from rest_framework import serializers
from hhback.api.models import Company, Vacancy


class CompanySerializer(serializers.Serializer):
    class Meta:
        model = Company
        fields = ('id', 'name')

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data.get('name'))
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class CompanySerializer2(serializers.ModelSerializer):
    description = serializers.CharField(allow_blank=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')


class VacancySerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company_id')


class CompanyWithVacancySerializer(serializers.ModelSerializer):
    vacancies = VacancySerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address', 'vacancies')