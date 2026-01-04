from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Patient(models.Model):
    GENDER_CHOICE = [('M', 'Male'),  ('F', 'Female')]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    visit_date = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Visit {self.reason} - {self.patient}"

class ClinicalNote(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, related_name='notes')
    subjective = models.TextField(blank=True) #S
    objective = models.TextField(blank=True)  #o
    assessment = models.TextField(blank=True)  #A
    plan = models.TextField(blank=True) #P

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Note for {self.visit} by Dr.{self.author}"