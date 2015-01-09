from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from list.views import home_page

# Create your tests here.

# class SmokeTest(TestCase):

# 	def test_bad_maths(self):
# 		self.assertEqual(1 + 1, 3)

class HomePageTest(TestCase):

	def test_root_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		#decode is used to convert the response.content bytes into a unicode string
		self.assertEqual(response.content.decode(), expected_html)

		#just remember that the response.content is going to be in bytes which is why we use b before
		#the string
		# self.assertTrue(response.content.startswith(b'<html>'))
		# self.assertIn(b'<title>To-Do lists</title>', response.content)
		# self.assertTrue(response.content.endswith(b'</html>'))

