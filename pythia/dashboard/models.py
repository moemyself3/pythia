from django.db import models


class ObsQueue(models.Model):
    queue_id = models.IntegerField(primary_key=True)
    survey_field = models.ForeignKey('SurveyField', models.DO_NOTHING, blank=False, null=False)

    class Meta:
        db_table = 'obs_queue'


class SurveyField(models.Model):
    survey_field_id = models.CharField(primary_key=True, max_length=6)
    ra = models.DecimalField(max_digits=10, decimal_places=6, blank=False, null=False)
    dec = models.DecimalField(max_digits=10, decimal_places=6, blank=False, null=False)
    l = models.DecimalField(max_digits=10, decimal_places=6, blank=False, null=False)
    b = models.DecimalField(max_digits=10, decimal_places=6, blank=False, null=False)
    program = models.CharField(max_length=255, blank=False, null=False)
    exposure_time = models.DecimalField(max_digits=10, decimal_places=6, blank=False, null=False)
    cadence = models.DecimalField(max_digits=10, decimal_places=6, blank=False, null=False)
    ephemeris = models.DecimalField(max_digits=10, decimal_places=6, blank=False, null=False)
    period = models.DecimalField(max_digits=10, decimal_places=6, blank=False, null=False)
    observations = models.IntegerField(blank=False, null=False)
    moon_phase = models.DecimalField(max_digits=10, decimal_places=6, blank=False, null=False)

    class Meta:
        db_table = 'survey_field'
