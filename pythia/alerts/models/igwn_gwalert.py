from django.db import models

from .notice import Notice


class GWAlert(models.Model):
    notice_id = models.ForeignKey('Notice', on_delete=models.CASCADE)
    alert_type = models.ForeignKey('AlertType', on_delete=models.CASCADE)
    time_created = models.DateTimeField()
    superevent_id = models.ForeignKey('SuperEvent', on_delete=models.CASCADE)
    urls = models.ForeignKey('GWAlertUrl', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    external_coinc = models.ForeignKey('ExternalCoinc', on_delete=models.CASCADE)

class AlertType(models.Model):
    alert_type = models.CharField(max_length=255)

class SuperEvent(models.Model):
    superevent_id = models.CharField(max_length=255)


class Event(models.Model):
    time = models.DateTimeField() 
    far = models.FloatField()
    significant = models.BooleanField()
    instruments = models.ForeignKey('EventInstrument', on_delete=models.CASCADE)
    group = models.ForeignKey('EventGroup', on_delete=models.CASCADE)
    pipeline = models.ForeignKey('EventPipeline', on_delete=models.CASCADE)
    search = models.ForeignKey('EventSearch', on_delete=models.CASCADE)
    properties = models.ForeignKey('EventProperties', on_delete=models.CASCADE)
    classification = models.ForeignKey('EventClassification', on_delete=models.CASCADE)
    duration = models.FloatField()
    central_frequency = models.FloatField()
    skymap = models.URLField()


class ExternalCoinc(models.Model):
    gcn_notice_id = models.BigIntegerField()
    ivorn = models.URLField()
    observatory = models.ForeignKey('ExternalCoincObservatory', on_delete=models.CASCADE)
    search = models.ForeignKey('ExternalCoincSearch', on_delete=models.CASCADE)
    time_difference = models.FloatField()
    time_coincidence_far = models.FloatField(),
    time_sky_position_coincidence_far = models.FloatField(),
    combined_skymap = models.URLField()


class GWAlertUrl(models.Model):
    gwalert_url = models.URLField()


class EventInstrument(models.Model):
    instrument = models.CharField(max_length=255)


class EventGroup(models.Model):
    group = models.CharField(max_length=255)


class EventPipeline(models.Model):
    pipeline = models.CharField(max_length=255)


class EventSearch(models.Model):
    search = models.CharField(max_length=255)


class EventProperties(models.Model):
    has_ns = models.FloatField()
    has_remnant = models.FloatField()
    has_mass_gap = models.FloatField()


class EventClassification(models.Model):
    bns = models.FloatField()
    nsbh = models.FloatField()
    bbh = models.FloatField()
    terrestrial = models.FloatField()


class ExternalCoincObservatory(models.Model):
    observatory = models.CharField(max_length=255)


class ExternalCoincSearch(models.Model):
    search = models.CharField(max_length=255)
