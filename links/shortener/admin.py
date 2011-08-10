from django.contrib import admin
from models import Url

class UrlAdmin(admin.ModelAdmin):
	"""This class is for helper method to deal with the Url Model"""
	pass

admin.site.register(Url, UrlAdmin)