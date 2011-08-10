from django.db import models

class Url(models.Model):
	"""This class will deal with storing the url and """
	url = models.CharField(max_length=5000)
	url_shortened = models.CharField(max_length=50)
	site = models.CharField(max_length=5000)
	date_added = models.DateTimeField()
	linked_count =  models.IntegerField()

	def __unicode__(self):
		return ('Shorten site at %s, linked %d times') % (self.site, self.linked_count)