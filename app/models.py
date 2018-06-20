from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from feincms.module.page.models import Page
from feincms.contents import RichTextContent
from feincms.module.medialibrary.contents import MediaFileContent

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

