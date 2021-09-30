# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Department(MPTTModel):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    director = models.ForeignKey(
        "hr.Staff",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="director",
        verbose_name=_("Director"),
    )
    slug = models.SlugField(verbose_name=_("slug"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Specialization")
        verbose_name_plural = _("Specializations")


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Name"))
    rate = models.CharField(max_length=100, verbose_name=_("Rate"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Position")
        verbose_name_plural = _("Positions")


class Staff(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_("First name"))
    middle_name = models.CharField(max_length=100, verbose_name=_("Middle name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last name"))
    date_birth = models.DateField(verbose_name=_("Birth day"))
    specialization = models.ForeignKey(
        Specialization, on_delete=models.PROTECT, verbose_name=_("Specialization")
    )
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, verbose_name=_("Department")
    )
    position = models.ForeignKey(
        Position, on_delete=models.PROTECT, verbose_name=_("Position")
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name=_("Category")
    )
    office = models.CharField(max_length=100, verbose_name=_("Office"))
    date_acceptance = models.DateField(verbose_name=_("Date of acceptance"))
    date_dismissal = models.DateField(
        null=True, blank=True, verbose_name=_("Date of dismissal")
    )
    time_working = models.TimeField(verbose_name=_("Working time"))
    time_reception = models.TimeField(verbose_name=_("Reception time"))
    date_contract_end = models.DateField(verbose_name=_("Contract completion date"))
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Staff")
        verbose_name_plural = _("Staff")


class Contact(models.Model):
    TYPE_CHOICES = (
        ("phone", _("Phone")),
        ("email", _("E-mail")),
        ("address", _("Address")),
        ("other", _("Other")),
    )
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_("Staff"))
    contact_type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, verbose_name=_("Type")
    )
    contact_value = models.CharField(max_length=100, verbose_name=_("Value"))

    def __str__(self):
        return f"{self.contact_type} {self.contact_value}"

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class Education(models.Model):
    TYPE_CHOICES = (
        ("courses", _("Сourses")),
        ("college", _("Сollege")),
        ("university", _("University")),
    )
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_("Staff"))
    education_type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, verbose_name=_("Type")
    )
    education_value = models.CharField(max_length=320, verbose_name=_("Value"))
    specialization = models.ForeignKey(
        Specialization, on_delete=models.PROTECT, verbose_name=_("Specialization")
    )

    def __str__(self):
        return f"{self.education_type} {self.education_value}"

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")


class File(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_("Staff"))
    name = models.CharField(max_length=320, verbose_name=_("Name"))
    desc = models.CharField(max_length=320, verbose_name=_("Description"))
    filename = models.FileField(verbose_name=_("File"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("File")
        verbose_name_plural = _("Files")


class Experience(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_("Staff"))
    name = models.CharField(max_length=320, verbose_name=_("Name"))
    city = models.CharField(max_length=100, verbose_name=_("City"))
    position = models.ForeignKey(
        "hr.Position", on_delete=models.PROTECT, verbose_name=_("Position")
    )
    date_start = models.DateField(verbose_name=_("Date start"))
    date_end = models.DateField(verbose_name=_("Date end"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Experience")
        verbose_name_plural = _("Experiences")


class PersonalRow(models.Model):
    TYPE_CHOICES = (("incentives", _("Incentives")), ("penalties", _("Penalties")))
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_("Staff"))
    row_type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, verbose_name=_("Row type")
    )
    row_value = models.CharField(max_length=320, verbose_name=_("Row data"))
    experience = models.ForeignKey(
        Experience, on_delete=models.PROTECT, verbose_name=_("Experience")
    )
    date = models.DateField(verbose_name=_("Date"))

    def __str__(self):
        return f"{self.row_type} {self.row_value}"

    class Meta:
        verbose_name = _("Personal row")
        verbose_name_plural = _("Personal rows")
