from django.contrib import admin
from django.utils import timezone
from .models import Culture, CultureContent
from mce_filebrowser.admin import MCEFilebrowserAdmin
# Register your models here.

class CultureAdmin(admin.ModelAdmin):
    list_display = ('culture_item', 'culture_tag')

class CulturedetailAdmin(MCEFilebrowserAdmin):
    list_display = ('culture_name', 'culture_headline', 'created_date', 'pub_date')

admin.site.register(Culture, CultureAdmin)
admin.site.register(CultureContent, CulturedetailAdmin)
