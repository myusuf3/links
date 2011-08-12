from django.db import models


class Domain(models.Model):
	site = models.CharField(max_length=5000)
	linked_count = models.IntegerField()
	date_updated = models.DateField()

	class Meta:
		ordering = ['-linked_count']

	def __unicode__(self):
		return ('%s linked %d') % (self.site, self.linked_count)

class Url(models.Model):
	"""This class will deal with storing the url and """
	url = models.CharField(max_length=5000)
	url_shortened = models.CharField(max_length=50)
	site = models.ForeignKey(Domain)
	date_time_created = models.DateTimeField()
	linked_count =  models.IntegerField()


	class Meta:
		ordering = ['-date_time_created']

	def __unicode__(self):
		return ('Shorten site at %s') % (self.site)

