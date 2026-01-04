from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from .models import Patient, Visit, ClinicalNote
from .serializer import  PatientSerializer, VisitSerializer, ClinicalNoteSerializer
from .permissions import IsDoctor, IsNurse, IsDoctorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsDoctorOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['first_name', ['last_name']]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [IsDoctor | IsNurse]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['patient', 'visit_date']
    search_field = ['reason']


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClinicalNoteViewSet(viewsets.ModelViewSet):
    queryset = ClinicalNote.objects.all()
    serializer_class = ClinicalNoteSerializer
    permission_classes = [IsDoctorOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_field = ['Subjective', 'Objective', "Assessment", "Plan"]

    def get_queryset(self):
        return ClinicalNote.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@login_required
def patient_list(request):
    q = request.GET.get('q', '')
    patients = Patient.objects.filter(
        Q(first_name_icontains=q) | Q(last_name__icontains=q) | Q(phone__icontains=q)) if q else Patient.objects.all()

    return render(request, 'patients/list.html', {'patients' : patients})

@login_required
def patient_search(request):
    q = request.GET.get('q', '')
    patients = Patient.objects.filter(
        Q(first_name_icontains=q) | Q(last_name__icontains=q) | Q(phone__icontains=q))
    return render(request, 'patients/list.html', {'patients': patients})
