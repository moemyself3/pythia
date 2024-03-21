from django.db import models


class Notice(models.Model):
    notice_id = models.BigAutoField(primary_key=True)
    topic = models.CharField(max_length=255, blank=False, null=False)
    timestamp = models.DateTimeField()
