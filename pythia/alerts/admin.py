from django.contrib import admin

from .models import Notice, GWAlert

# Register your models here.
admin.site.register(Notice)
admin.site.register(GWAlert)
