import urlparse
from datetime import datetime # TODO make this better, it sucks

import requests
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponsePermanentRedirect

from shortener.models import Url
from shortener.forms import ShortenForm


def shorten_algo(url):
	"""This is the shortened url algorithm, this will take the given url, 
	   and return a shorter one.
	"""
	pass

def make_url_model(url, site): 
	""" This should on occur once per newly created URL, the linked count is set to zero if it
		is a new site added to database
	"""
	url_model = Url()
	url_model.url = url
	url_shorturl  = url
	url_model.url_shortened = url_short
	url_model.date_added = datetime.now()
	url_model.linked_count = 0
	url_model.save()

def submitted_check(url):
	"""This method will check to see if the url has been already been submitted
	   It will return that shorten_url and increment count.
	"""
	url_model = Url.objects.get(url=url)
	if url_model:
		print url_model.url_shortened
		#TODO check for if the 'site' is same then increment
		url_model.linked_count += 1
		return True
	else:
		return False

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
			#print form.cleaned_data
			url = form.cleaned_data['url']
			url_shortened = form.clean_data['url']
			#submitted_check(url)
			site = strip_to_domain(url)
			make_url_model(url, site)

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