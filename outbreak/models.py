"""
outbreak models.
"""
from django.db import models as djangomodels
from django.db.models import fields

from opal import models
from opal.core.fields import ForeignKeyOrFreeText
from opal.core import lookuplists


class Findings_rash_type(lookuplists.LookupList):
    class Meta:
        verbose_name = "Findings rash type"


class Findings_rash_distribution(lookuplists.LookupList):
    class Meta:
        verbose_name = "Findings rash distribution"



class Demographics(models.Demographics):
    fuzzy_age = fields.CharField(max_length=255, blank=True, null=True)

class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass


class PresentingSymptoms(models.EpisodeSubrecord):
    _title = 'Presenting Symptoms'
    _icon = 'fa fa-stethoscope'

    symptoms = djangomodels.ManyToManyField(models.Symptom, related_name="presenting_complaints")
    duration = fields.CharField(max_length=255, blank=True, null=True)
    details = fields.TextField(blank=True, null=True)


    def to_dict(self, user):
        field_names = self.__class__._get_fieldnames_to_serialize()
        result = {
            i: getattr(self, i) for i in field_names if not i == "symptoms"
        }
        result["symptoms"] = list(self.symptoms.values_list("name", flat=True))
        return result

    @classmethod
    def _get_fieldnames_to_serialize(cls):
        field_names = super(PresentingSymptoms, cls)._get_fieldnames_to_serialize()
        removed_fields = {u'symptom_fk_id', 'symptom_ft', 'symptom'}
        field_names = [i for i in field_names if i not in removed_fields]
        return field_names


class PatientHistory(models.EpisodeSubrecord):
    social_history = fields.TextField(blank=True, null=True)
    unwell_contact = fields.NullBooleanField()
    immunisations_up_to_date = fields.NullBooleanField()


class Examination(models.EpisodeSubrecord):
    _title        = 'Examination'
    _icon         = 'fa fa-stethoscope'

    lymphadenopathy         = fields.CharField(max_length=20, blank=True, null=True)
    lymphadenopathy_details = fields.CharField(max_length=255, blank=True, null=True)
    jaundice                = fields.CharField(max_length=20, blank=True)
    dehydration             = fields.CharField(max_length=20, blank=True)

    rash                    = fields.CharField(max_length=20, blank=True)
    rash_type               = ForeignKeyOrFreeText(Findings_rash_type)
    rash_distribution       = ForeignKeyOrFreeText(Findings_rash_distribution)

    cardiovascular          = fields.CharField(max_length=255, blank=True, null=True)
    respiratory             = fields.CharField(max_length=255, blank=True, null=True)
    abdominal               = fields.CharField(max_length=255, blank=True, null=True)
    oropharnyx              = fields.CharField(max_length=255, blank=True, null=True)
    neurological            = fields.CharField(max_length=255, blank=True, null=True)
    other_findings          = fields.CharField(max_length=255, blank=True, null=True)
