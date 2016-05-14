"""
Pathways for outbreak app
"""
from pathway import pathways

from outbreak import models
from obs import models as obsmodels

class TriagePathway(pathways.UnrolledPathway):
    display_name = 'Triage patient'
    slug = 'triage'

    steps = (
        pathways.DemographicsStep(model=models.Demographics),

        models.PresentingSymptoms,

        pathways.MultSaveStep(model=models.PastMedicalHistory),

        pathways.MultSaveStep(models.Allergies),
        models.PatientHistory,

        models.Examination,


        pathways.MultSaveStep(model=obsmodels.Observation),
        # pathways.MultSaveStep(model=models.Investigation),
        # pathways.MultSaveStep(model=models.Treatment)
    )
