from django.contrib import admin
from .models import Post, Vulner
from mptt.admin import MPTTModelAdmin
from feincms.admin import tree_editor

admin.site.register(Post)
# Register your models here.

class VulnerAdmin(tree_editor.TreeEditor):
    fields = ['id', 'name', 'parent']
    list_display = ["name", "actions_column", ]
    search_fields = ('name', )
 
    mptt_level_indent = 15
 
admin.site.register(Vulner, VulnerAdmin)