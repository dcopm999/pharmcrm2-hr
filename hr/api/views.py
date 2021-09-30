from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from hr import models
from hr.api import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [DjangoModelPermissions]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [DjangoModelPermissions]


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    permission_classes = [DjangoModelPermissions]


class PositionViewSet(viewsets.ModelViewSet):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer
    permission_classes = [DjangoModelPermissions]


class StaffViewSet(viewsets.ModelViewSet):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_classes = [DjangoModelPermissions]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [DjangoModelPermissions]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer
    permission_classes = [DjangoModelPermissions]


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = models.Experience.objects.all()
    serializer_class = serializers.ExperienceSerializer
    permission_classes = [DjangoModelPermissions]


class PersonalRowViewSet(viewsets.ModelViewSet):
    queryset = models.PersonalRow.objects.all()
    serializer_class = serializers.PersonalRowSerializer
    permission_classes = [DjangoModelPermissions]
