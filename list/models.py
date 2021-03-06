from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class List(models.Model):

	def get_absolute_url(self):
		"""Fuction that will return the absolute url for an object. Requires a named URL"""
		return reverse('view_list', args=[self.id])

class Item(models.Model):
	text = models.TextField(default='', blank=False)
	list = models.ForeignKey(List, default=None)
