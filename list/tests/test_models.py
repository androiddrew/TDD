from django.test import TestCase
from django.core.exceptions import ValidationError
from list.models import Item, List

class ListAndItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(first_saved_item.list, list_)
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(second_saved_item.list, list_)

	def test_cannot_save_empty_list_items(self):
		list_ = List.objects.create()
		item = Item(text='', list=list_)

		#We could use try catch blocks but context managers are more easily read as you can 
		#See below when we are using the with statement
		# try: item.save()
		# 	self.fail('The save should have raised an exception')
		# except ValidationError:
		# 	pass

		with self.assertRaises(ValidationError):
			item.save()
			#Django method to run full Validation
			item.full_clean()