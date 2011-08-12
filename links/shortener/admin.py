from django.contrib import admin
from models import Url, Domain

class UrlAdmin(admin.ModelAdmin):
	"""This class is for helper method to deal with the Url Model"""
	pass

class DomainAdmin(admin.ModelAdmin):
	pass

admin.site.register(Domain, DomainAdmin)	
admin.site.register(Url, UrlAdmin)