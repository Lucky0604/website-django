from django.contrib import admin
from django.utils import timezone
from .models import Company, Author, Content, CompanyImage
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'tagline')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'email')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('headline', 'company_name', 'created_date', 'pub_date')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(CompanyImage)
