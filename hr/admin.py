# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from mptt.admin import MPTTModelAdmin

from hr import models


class StaffInline(admin.StackedInline):
    model = models.Staff
    extra = 1


class ExperienceInline(admin.StackedInline):
    model = models.Experience
    suit_classes = "suit-tab suit-tab-experience"
    autocomplete_fields = ["position"]
    extra = 1


class PersonalRowInline(admin.TabularInline):
    model = models.PersonalRow
    suit_classes = "suit-tab suit-tab-personalrow"
    extra = 1


class ContactInline(admin.TabularInline):
    model = models.Contact
    suit_classes = "suit-tab suit-tab-contact"
    extra = 1


class EducationInline(admin.TabularInline):
    model = models.Education
    autocomplete_fields = ["specialization"]
    suit_classes = "suit-tab suit-tab-education"
    extra = 1


class FileInline(admin.TabularInline):
    model = models.File
    suit_classes = "suit-tab suit-tab-file"
    extra = 1


@admin.register(models.Department)
class DepartmentAdmin(MPTTModelAdmin):
    inlines = [StaffInline]
    mptt_level_indent = 20
    list_display = ["name"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    inlines = [StaffInline]
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [
        ContactInline,
        EducationInline,
        FileInline,
        ExperienceInline,
        PersonalRowInline,
    ]
    list_display = [
        "last_name",
        "first_name",
        "middle_name",
        "department",
        "specialization",
    ]
    autocomplete_fields = ["department", "position", "specialization"]
    suit_form_tabs = (
        ("general", _("General")),
        ("contact", _("Contacts")),
        ("education", _("Educations")),
        ("file", _("Files")),
        ("experience", _("Experiences")),
        ("personalrow", _("Personal Rows")),
    )

    fieldsets = [
        (
            None,
            {
                "classes": [
                    "suit-tab",
                    "suit-tab-general",
                ],
                "fields": [
                    "last_name",
                    "first_name",
                    "middle_name",
                    "date_birth",
                ],
            },
        ),
        (
            None,
            {
                "classes": [
                    "suit-tab",
                    "suit-tab-general",
                ],
                "fields": [
                    "department",
                    "position",
                    "specialization",
                    "office",
                ],
            },
        ),
        (
            None,
            {
                "classes": (
                    "suit-tab",
                    "suit-tab-general",
                ),
                "fields": [
                    "date_acceptance",
                    "date_dismissal",
                    "time_working",
                    "time_reception",
                    "date_contract_end",
                ],
            },
        ),
    ]
