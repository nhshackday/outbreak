"""
Defining OPAL PatientLists
"""
from opal import core
from opal.models import Episode

from outbreak import models

class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'
    template_name = 'patient_list.html'

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Drugs
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()
