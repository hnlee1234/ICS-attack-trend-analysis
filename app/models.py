from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from feincms.module.page.models import Page
from feincms.contents import RichTextContent
from feincms.module.medialibrary.contents import MediaFileContent
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Vulner(MPTTModel):
	id = models.CharField(max_length=50, unique=True, primary_key = True)
	name = models.CharField(max_length=200)
	severity = models.CharField(max_length=20, null=True, blank=True)
	link = models.CharField(max_length=200, blank=True, null=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


	class MPTTMeta:
		order_insertion_by = ['id']

	def __str__(self):
		return self.name


#feinCMS-------------------------------------------------------------------------------------------------------------
	Page.register_extensions(
		'feincms.extensions.datepublisher',
		'feincms.extensions.translations'
	) # Example set of extensions
	Page.register_templates({
		'title': _('Standard template'),
		'path': 'base.html',
		'regions': (
			('main', _('Main content area')),
			('sidebar', _('Sidebar'), 'inherited'),
		),
	})
	Page.create_content_type(RichTextContent)
	Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
		('default', _('default')),
		('lightbox', _('lightbox')),
	))
#------------------------------------------------------------------------------------------------------------------

class Company(MPTTModel):
	name = models.CharField(max_length = 100, primary_key=True)
	iscompany = models.BooleanField(default=True)
	url = models.CharField(max_length=200, blank=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
	
	paper1 = models.CharField(max_length=150, blank=True)
	paper2 = models.CharField(max_length=150, blank=True)
	refer = models.CharField(max_length=150, blank=True)
	relation_level = models.CharField(max_length=50, blank=True)
	main_division = models.CharField(max_length=50, blank=True)
	sub_division = models.CharField(max_length=50, blank=True)
	

	class MPTTMeta:
		order_insertion_by = ['name']
	
	def __str__(self):
		return self.name

	#feinCMS-------------------------------------------------------------------------------------------------------------
	Page.register_extensions(
		'feincms.extensions.datepublisher',
		'feincms.extensions.translations'
	) # Example set of extensions
	Page.register_templates({
		'title': _('Standard template'),
		'path': 'base.html',
		'regions': (
			('main', _('Main content area')),
			('sidebar', _('Sidebar'), 'inherited'),
		),
	})
	#-------------------------------------------------------------------------------------------------------------------

class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, db_index=True, primary_key=True)
    company = TreeForeignKey('Company', null=True, blank=True, on_delete=models.CASCADE)
    paper1 = models.CharField(max_length=150, blank=True)
    paper2 = models.CharField(max_length=150, blank=True)
    refer = models.CharField(max_length=150, blank=True)
    relation_level = models.CharField(max_length=50, blank=True)
    main_division = models.CharField(max_length=50, blank=True)
    sub_division = models.CharField(max_length=50, blank=True)
 
    def __str__(self):
        return self.name

'''
class Test(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE, default=str(timezone.now))
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class TreeItem(MPTTModel):
    name = models.CharField(max_length = 50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete = models.CASCADE)
'''

