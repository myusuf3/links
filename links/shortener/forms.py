import re
import urlparse 

from datetime import datetime # TODO make this better, it sucks
from datetime import timedelta
from datetime import date

import requests
from django import forms

from models import Url, Domain



def strip_to_domain(url):
	""" This method will remove the extra bits and reviel the hostname, 
		This method is needed for keeping track of site popularity.

		all subdomains such as blog and about will be handled as different sites.
		www. will be considered same as base site.

		www.example.com and example.com are the same. while blog.example.com is different
	"""
	hostname = urlparse.urlparse(url).hostname
	if hostname.startswith('www.'):
		hostname = re.sub('^www\.', '', hostname)
	return hostname


def submitted_check(url):
	"""This method will check to see if the url has been already been submitted
	   It will return that shorten_url and increment count.
	"""
	try:
		url_model = Url.objects.get(url=url)
	except:
		return {'submitted': False} 
	print url_model.url_shortened

	site = strip_to_domain(url)
	#checking domain to see if has been linked  for top domains page
	try:
		domain = Domain.objects.get(site=site)
	except:
		pass
	domain.linked_count += 1
	domain.save()
	


	if url_model.domain.date_updated.month == date.today().month:
		print 'same_month'
		url_model.domain.date_updated = date.today()
		url_model.linked_count += 1
		url_model.save()
		domain.save()
	else:
		print 'different_month'
		url_model.domain.date_updated = date.today()
		url_model.domain.linked_count = 1
		url_model.save()
		domain.save()
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
		