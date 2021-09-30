#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pharmcrm2-hr
------------

Tests for `pharmcrm2-hr` models module.
"""

from django.test import TestCase

from hr import models
from tests import factories


class StaffModelsCase(TestCase):
    def setUp(self):
        factories.StaffFactory()

    def test_str(self):
        query = models.Staff.objects.last()
        self.assertEqual(
            query.__str__(), f"{query.last_name} {query.first_name} {query.middle_name}"
        )


class CategoryModelCase(TestCase):
    def setUp(self):
        factories.CategoryFactory()

    def test_str(self):
        query = models.Category.objects.last()
        self.assertEqual(query.__str__(), query.name)


class DepartmentModelCase(TestCase):
    def setUp(self):
        factories.DepartmentFactory()

    def test_str(self):
        query = models.Department.objects.last()
        self.assertEqual(query.__str__(), query.name)


class SpecializationModelCase(TestCase):
    def setUp(self):
        factories.SpecializationFactory()

    def test_str(self):
        query = models.Specialization.objects.last()
        self.assertEqual(query.__str__(), query.name)


class PositionModelCase(TestCase):
    def setUp(self):
        factories.PositionFactory()

    def test__str(self):
        query = models.Position.objects.last()
        self.assertEqual(query.__str__(), query.name)


class ContactModelCase(TestCase):
    def setUp(self):
        factories.ContactFactory()

    def test_str(self):
        query = models.Contact.objects.last()
        self.assertEqual(query.__str__(), f"{query.contact_type} {query.contact_value}")


class EducationModelCase(TestCase):
    def setUp(self):
        factories.EducationFactory()

    def test_str(self):
        query = models.Education.objects.last()
        self.assertEqual(
            query.__str__(), f"{query.education_type} {query.education_value}"
        )


class FileModelCase(TestCase):
    def setUp(self):
        factories.FileFactory()

    def test_str(self):
        query = models.File.objects.last()
        self.assertEqual(query.__str__(), query.name)


class ExperienceModelCase(TestCase):
    def setUp(self):
        factories.ExperienceFactory()

    def test_str(self):
        query = models.Experience.objects.last()
        self.assertEqual(query.__str__(), query.name)


class PersonalRowModelCase(TestCase):
    def setUp(self):
        factories.PersonalRowFactory()

    def test_str(self):
        query = models.PersonalRow.objects.last()
        self.assertEqual(query.__str__(), f"{query.row_type} {query.row_value}")
