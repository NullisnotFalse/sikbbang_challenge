from django.contrib import admin
from .models import ChallangeModel

class TimeDisplay(admin.ModelAdmin):
    list_display = ('content','image','created_at','updated_at',)
    fields =('content','image','created_at','updated_at',)
    readonly_fields = ('created_at','updated_at')

# Register your models here.
admin.site.register(ChallangeModel,TimeDisplay)