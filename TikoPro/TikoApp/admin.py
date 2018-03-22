from django.contrib import admin
from .models import Profile,EventType,Event,Tags

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Profile)
admin.site.register(EventType)
admin.site.register(Event,EventAdmin)
admin.site.register(Tags)
