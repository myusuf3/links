import urlparse
from datetime import datetime # TODO make this better, it sucks

import requests
from django.http import HttpResponseRedirect
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
	url_short  = url
	url_model.url_shortened = url_short
	url_model.site = strip_to_domain(url)
	url_model.date_added = datetime.now()
	url_model.linked_count = 0
	url_model.save()



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
			url_shortened = form.cleaned_data['url']
			site = strip_to_domain(url)
			make_url_model(url, site)
			return HttpResponseRedirect('/thanks/')

	else:
		form = ShortenForm()
	return render (request, 'index.html',  {'form':form})


def thanks(request):
	"""This view returns the shortened url back to the client.
	"""


def list_hundred_popular(request):
	""" Returns the hundred most popular, by the amount being linked to. 
	"""
	url_list = Url.objects.order_by('-linked_count')[:100]
	return render(request, 'tophundred.html', {'url_list': url_list})


def redirect_link(request, code):
	"""This view is reponsible for decoding the hashcode and redirect to url page.

	Keyword arguments:
	hashcode -- shortcut used to look up corresponding url page

	"""
	pass

	# file_request = get_object_or_404(Url, code=code)
	# 	return redirect(url) 
	# else:
	# 	raise Http404