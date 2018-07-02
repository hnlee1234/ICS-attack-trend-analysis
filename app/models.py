from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from feincms.module.page.models import Page
from feincms.contents import RichTextContent
from feincms.module.medialibrary.contents import MediaFileContent

'''
class Post(models.Model):
	"""docstring for Post"""
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
'''
# Create your models here.
class Vulner(MPTTModel):
	id = models.CharField(max_length=50, unique=True, primary_key = True)
	name = models.CharField(max_length=200)
	severity = models.CharField(max_length=20, null=True, blank=True)
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
	name = models.CharField(max_length = 50, primary_key=True)
	url = models.CharField(max_length=200, blank=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)

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