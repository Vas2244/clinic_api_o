from rest_framework import serializers
from .models import Patient, Visit, ClinicalNote

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('created_by',)

class VisitSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient', read_only=True)

    class Meta:
        model = Visit
        fields = '__all__'
        read_only_fields = ('created_by',)

class ClinicalNoteSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    visit_info = serializers.CharField(source='visit', read_only=True)

    class Meta:
        model = ClinicalNote
        fields = '__all__'
        read_only_fields = ('author',)

