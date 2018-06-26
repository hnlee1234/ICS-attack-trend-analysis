from django.contrib import admin
from .models import Vulner, Company, Product
from mptt.admin import MPTTModelAdmin
from feincms.admin import tree_editor

#admin.site.register(Post)
# Register your models here.

class VulnerAdmin(tree_editor.TreeEditor):
    fields = ['id', 'name', 'severity', 'parent']
    list_display = ["title", "id", "severity", "actions_column", ]
    search_fields = ('id', )
 
    mptt_level_indent = 30
 
class CompanyAdmin(tree_editor.TreeEditor):
    fields = ['name', 'url', 'parent', 'actions_column']
    list_display = ('name', 'url')
 
    mptt_level_indent = 20

class ProductAdmin(admin.ModelAdmin):
    ordering = ('name',)
    fields = ['name', 'company', 'relation_level', 'main_division', 'sub_division', 'paper1', 'paper2', 'refer']
    # change_list_template = 'admin/product_change_list.html'
    list_display = ('name', 'company', 'relation_level', 'main_division', 'sub_division')
    search_fields = ['name']
 
    list_filter = ('name',)
 
 
admin.site.register(Product, ProductAdmin)
admin.site.register(Vulner, VulnerAdmin)
admin.site.register(Company, CompanyAdmin)