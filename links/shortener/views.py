import urlparse
from datetime import datetime # TODO make this better, it sucks

import requests
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponsePermanentRedirect

from shortener.models import Url
from shortener.forms import ShortenForm



def submitted_check(url):
	"""This method will check to see if the url has been already been submitted
	   It will return that shorten_url and increment count.
	"""
	url_model = Url.objects.get(url=url)
	print url_model.url_shortened

def strip_to_domain(url):
	""" This method will remove the extra bits and reviel the hostname, 
		This method is needed for keeping track of site popularity
	"""
	hostname = urlparse.urlparse(url).hostname
	return hostname



def homepage(request):
	""" This view is responsible for displaying the landing page
		with the shortening form.

		This page has three flows:
		first -- post method for accepting the url to be shortened
		second -- if not post show form
		third -- error in submitted form

	Keyword arguments:

	"""
	if request.method == 'POST':
		form = ShortenForm(request.POST)
		
		if form.is_valid():
			print form.cleaned_data
			url_model = Url()
			submitted_check
			url = form.cleaned_data['url']
			site = strip_to_domain(url)
			link_date = datetime.now()

	else:
		form = ShortenForm()
	return render (request, 'index.html',  {'form':form})





def redirect_link(request, sha1):
	"""This view is reponsible for decoding the hashcode and redirect to url page.

	Keyword arguments:
	hashcode -- shortcut used to look up corresponding url page

	"""

	file_request = get_object_or_404(Url, sha1=sha1)
	if file_request.user == request.user:
		url  = file_request.file_loaded.url
		#redirects the browser to the file in order to download
		return redirect(url) 
	else:
		raise Http404