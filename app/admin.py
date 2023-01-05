from django.contrib import admin
from .models import * 

class MapsAdmin(admin.ModelAdmin):
    list_display = ['alamat']

class CrudAdmin(admin.ModelAdmin):
    list_display = ['nama']


admin.site.register(Maps, MapsAdmin)
admin.site.register(Crud, CrudAdmin)