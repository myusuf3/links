import requests
from django import forms

from models import Url


def submitted_check(url):
	"""This method will check to see if the url has been already been submitted
	   It will return that shorten_url and increment count.
	"""
	try:
		url_model = Url.objects.get(url=url)
	except:
		return {'submitted': False} 
	print url_model.url_shortened
	#TODO check for if the 'site' is same then increment
	url_model.linked_count += 1
	url_model.save()
	return {'submitted': True, 'url_model': url_model}

class ShortenForm(forms.Form):
	url = forms.CharField(max_length=500, label='Link')

	def clean_url(self):
		""" This will us to return the request code for submitted page, and
			check to see if it returns a 200 code. If so allow else reject.
		"""
		url = self.cleaned_data['url']
		result = {}
		result = submitted_check(url)
		submitted = result['submitted']
		print submitted
		if submitted:
			url_model = result['url_model']
			print url_model
			raise forms.ValidationError('Link has been shortened %s' % (url_model.url_shortened))
		if url.startswith('http://'):
			pass
		else:
			raise forms.ValidationError('Link must begin with http://')
		result = requests.get(url)
		if result.status_code is 200:
			return self.cleaned_data['url']
		else:
			raise forms.ValidationError('Links must return a 200 status code')
		