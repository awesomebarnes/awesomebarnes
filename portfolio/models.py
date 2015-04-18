from django.db.models import CharField, TextField
from adminsortable.models import Sortable
from autoslug import AutoSlugField
from filer.fields.image import FilerImageField

class PortfolioItem(Sortable):
	slug = AutoSlugField(populate_from='name')
	name = CharField(max_length=50, blank=False, null=False)
	caption = CharField(max_length=250, blank=True, null=True)
	image = FilerImageField(null=True, blank=True)
	description = TextField(max_length=1000, blank=True, null=True)

	class Meta(Sortable.Meta):
		verbose_name = "Portfolio item"
		verbose_name_plural = "Portfolio items"

	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.__str__()
