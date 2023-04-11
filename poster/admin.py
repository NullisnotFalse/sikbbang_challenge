from django.contrib import admin
from .models import PosterModel

class TimeDisplay(admin.ModelAdmin):
    list_display = ('writer','title','content','image','created_at','updated_at',)
    fields =('writer','title','content','image','created_at','updated_at',)
    readonly_fields = ('created_at','updated_at')

# Register your models here.
admin.site.register(PosterModel,TimeDisplay)