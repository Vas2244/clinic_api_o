from django.contrib import admin
from .models import Patient, Visit, ClinicalNote
# Register your models here.

@admin.register(Patient)
class PatientName(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gender')
    search_fields = ('first_name', 'last_name')

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('patient', 'reason', 'visit_date')
    list_filter = ('visit_date',)

@admin.register(ClinicalNote)
class ClinicalNoteAdmin(admin.ModelAdmin):
    list_display = ('visit', 'author', 'created_at')
