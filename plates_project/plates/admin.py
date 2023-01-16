from django.contrib import admin
from .models import Plate

class PlateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'createdAt')


admin.site.register(Plate, PlateAdmin)
# admin.site.register(User)
