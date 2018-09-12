from django.contrib import admin
from .models import Vulner, Company, Product
from mptt.admin import MPTTModelAdmin
from feincms.admin import tree_editor
from django.contrib.contenttypes.admin import GenericTabularInline

#admin.site.register(Post)
# Register your models here.

class VulnerAdmin(tree_editor.TreeEditor):
    fields = ['id', 'name', 'severity', 'parent', 'link',]
    list_display = ["title", "id", "severity", "actions_column", ]
    search_fields = ('id', 'name')
 
    mptt_level_indent = 30
 
class CompanyAdmin(tree_editor.TreeEditor):
    fields = ['name', 'iscompany', 'url', 'relation_level', 'main_division', 'sub_division', 'paper1', 'paper2', 'refer', 'parent']
    list_display = ('name','main_division', 'sub_division',  'actions_column')
 
    mptt_level_indent = 20

class ProductAdmin(admin.ModelAdmin):
    ordering = ('name',)
    fields = ['name', 'company', 'relation_level', 'main_division', 'sub_division', 'paper1', 'paper2', 'refer']
    # change_list_template = 'admin/product_change_list.html'
    list_display = ('company', 'relation_level', 'main_division', 'sub_division')
    search_fields = ['name', 'sub_division']
 
    list_filter = ('company', 'sub_division')
 
'''
class TestInline(GenericTabularInline):
    model = Test
    fields = ['name',]


class TreeAdmin(admin.ModelAdmin):
    inlines = [TestInline,]
    fields = ['name',]


class TestAdmin(admin.ModelAdmin):
    fields = ['name','type']
    list_display = ('name','type')
'''

admin.site.register(Product, ProductAdmin)
admin.site.register(Vulner, VulnerAdmin)
admin.site.register(Company, CompanyAdmin)
'''
admin.site.register(TreeItem, TreeAdmin)
admin.site.register(Test, TestAdmin)
'''
