import requests

from django import forms


class ShortenForm(forms.Form):
	url = forms.CharField(max_length=500, label='Link')

def clean_url(self):
	""" This will us to return the request code for submitted page, and
		check to see if it returns a 200 code. If so allow else reject.
	"""
	url = self.cleaned_data['url']
	if url.startswith('http://'):
		pass
	else:
		raise forms.ValidationError('Link must begin with http://')
	result = requests.get()
	if result.status_code is '200':
		return self.cleaned_data['url']
	else:
		raise forms.ValidationError('Links must be valid')
		