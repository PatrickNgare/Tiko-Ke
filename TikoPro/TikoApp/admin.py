from django.contrib import admin
from .models import Profile,EventType,Event

# Register your models here.
admin.site.register(Profile)
admin.site.register(EventType)
admin.site.register(Event)

