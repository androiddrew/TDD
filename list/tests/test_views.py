from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

#removing from test scripts since we are no longer using hard coded requests to views
#Instead we are using the django test client
from list.views import home_page
from list.models import Item, List


class NewListTest(TestCase):

	def test_can_save_a_POST_request_to_an_existing_list(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		self.client.post('/lists/%d/add_item' %(correct_list.id,), data={'item_text':'A new item for an existing list'})

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new item for an existing list')
		self.assertEqual(new_item.list, correct_list)

	def test_redirects_to_list_view(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		response = self.client.post('/lists/%d/add_item' %(correct_list.id,), data={'item_text':'A new item for an existing list'})

		self.assertRedirects(response, '/lists/%d/' %(correct_list.id))

	def test_saving_a_POST_request(self):
		# commenting this out because we could use the test client provided by django instead
		# request = HttpRequest()
		# request.method = 'POST'
		# request.POST['item_text'] = 'A new list item'

		#response = home_page(request)
		
		#here we are using the client to submit a post to the following URL with data
		self.client.post('/lists/new', data = {'item_text': 'A new list item'})

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')

	def test_redirects_after_POST(self):
		# Once again we are goint to use the Django client instead to get the response of a post
		# request = HttpRequest()
		# request.method = 'POST'
		# request.POST['item_text'] = 'A new list item'

		# response = home_page(request)

		response = self.client.post('/lists/new', data = {'item_text': 'A new list item'})
		new_list = List.objects.first()

		#This code will not work with the django client because the client uses the full stack 
		#appending the relative URL to the path 
		#self.assertEqual(response.status_code, 302)
		#self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
		self.assertRedirects(response, '/lists/%d/' %(new_list.id))

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

	#HOME PAGE NO LONGER HANDLES POST REQUESTS
	# def test_saving_and_retrieving_items(self):
	# 	first_item = Item()
	# 	first_item.text = 'The first (ever) list item'
	# 	first_item.save()

	# 	second_item = Item()
	# 	second_item.text = 'Item the second'
	# 	second_item.save()

	# 	saved_items = Item.objects.all()
	# 	self.assertEqual(saved_items.count(), 2)

	# 	first_saved_item = saved_items[0]
	# 	second_saved_item = saved_items[1]
	# 	self.assertEqual(first_saved_item.text, 'The first (ever) list item')
	# 	self.assertEqual(second_saved_item.text, 'Item the second')


	# def test_home_page_only_saves_items_when_necessary(self):
	# 	request = HttpRequest()
	# 	home_page(request)
	# 	self.assertEqual(Item.objects.count(), 0)

class ListViewTest(TestCase):

	def test_displays_all_items(self):
		correct_list = List.objects.create()
		Item.objects.create(text='itemey 1', list=correct_list)
		Item.objects.create(text='itemey 2', list=correct_list)

		other_list = List.objects.create()
		Item.objects.create(text='other list items 1', list=other_list)
		Item.objects.create(text='other list items 2', list=other_list)
		#removal of calling the view function directly and relying on the test case provided by Django
		#request = HttpRequest()
		#response = home_page(request)
		response = self.client.get('/lists/%d/' %(correct_list.id))


		#Instead of messing witht eh Assert in /b string dance we are using the Contains function which
		#Covers all of that
		#self.assertIn('itemey 1', response.content.decode())
		#self.assertIn('itemey 2', response.content.decode())

		self.assertContains(response, 'itemey 1')
		self.assertContains(response, 'itemey 2')
		self.assertNotContains(response, 'other list items 1')
		self.assertNotContains(response, 'other list items 2')

	def test_uses_list_template(self):
		list_ = List.objects.create()
		response = self.client.get('/lists/%d/' %(list_.id,))
		self.assertTemplateUsed(response, 'list.html')

	def test_passes_correct_list_to_template(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.get('/lists/%d/' % (correct_list.id))
		self.assertEqual(response.context['list'], correct_list)
