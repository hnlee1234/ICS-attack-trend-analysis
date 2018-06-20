from django.contrib import admin
from .models import Post, Vulner
from mptt.admin import MPTTModelAdmin
from feincms.admin import tree_editor

admin.site.register(Post)
# Register your models here.

class VulnerAdmin(tree_editor.TreeEditor):
    fields = ['id', 'name', 'severity', 'parent']
    list_display = ["title", "id", "severity", "actions_column", ]
    search_fields = ('id', )
 
    mptt_level_indent = 30
 
admin.site.register(Vulner, VulnerAdmin)