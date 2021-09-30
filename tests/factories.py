from random import randint

import factory
from factory.django import DjangoModelFactory

from hr import models

factory.Faker._DEFAULT_LOCALE = "ru_RU"


class CategoryFactory(DjangoModelFactory):
    name = factory.Faker("bs")

    class Meta:
        model = models.Category


class DepartmentFactory(DjangoModelFactory):
    name = factory.Faker("catch_phrase")

    class Meta:
        model = models.Department


class SpecializationFactory(DjangoModelFactory):
    name = factory.Faker("job")

    class Meta:
        model = models.Specialization


class PositionFactory(DjangoModelFactory):
    name = factory.Faker("job")
    rate = "123"

    class Meta:
        model = models.Position


class StaffFactory(DjangoModelFactory):
    first_name = factory.Faker("first_name")
    middle_name = factory.Faker("middle_name")
    last_name = factory.Faker("last_name")
    date_birth = factory.Faker("date_of_birth")
    department = factory.SubFactory(DepartmentFactory)
    specialization = factory.SubFactory(SpecializationFactory)
    category = factory.SubFactory(CategoryFactory)
    position = factory.SubFactory(PositionFactory)
    office = randint(1, 500)
    date_acceptance = factory.Faker("date")
    date_dismissal = factory.Faker("future_date")
    time_working = "09:00:00"
    time_reception = "11:00:00"
    date_contract_end = factory.Faker("future_date")

    class Meta:
        model = models.Staff


class ContactFactory(DjangoModelFactory):
    staff = factory.SubFactory(StaffFactory)
    contact_type = "phone"
    contact_value = factory.Faker("phone_number")

    class Meta:
        model = models.Contact


class EducationFactory(DjangoModelFactory):
    staff = factory.SubFactory(StaffFactory)
    education_type = "courses"
    education_value = factory.Faker("job")
    specialization = factory.SubFactory(SpecializationFactory)

    class Meta:
        model = models.Education


class FileFactory(DjangoModelFactory):
    staff = factory.SubFactory(StaffFactory)
    name = factory.Faker("file_name")
    desc = factory.Faker("bs")
    filename = factory.Faker("file_path")

    class Meta:
        model = models.File


class ExperienceFactory(DjangoModelFactory):
    staff = factory.SubFactory(StaffFactory)
    name = factory.Faker("company")
    city = factory.Faker("city")
    position = factory.SubFactory(PositionFactory)
    date_start = factory.Faker("date")
    date_end = factory.Faker("date")

    class Meta:
        model = models.Experience


class PersonalRowFactory(DjangoModelFactory):
    staff = factory.SubFactory(StaffFactory)
    row_type = "incentives"
    row_value = factory.Faker("company")
    experience = factory.SubFactory(ExperienceFactory)
    date = factory.Faker("date")

    class Meta:
        model = models.PersonalRow
