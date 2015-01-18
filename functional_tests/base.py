from django.contrib.staticfiles.testing import StaticLiveServerTestCase # Used for Static file testing
from selenium import webdriver
import sys


class FunctionalTest(StaticLiveServerTestCase):
	"""Base class for Functional testing in Django using selenium"""
	@classmethod
	def setUpClass(cls): #
		for arg in sys.argv: #
			if 'liveserver' in arg: #
				cls.server_url = 'http://' + arg.split('=')[1] # 
				return #
		super().setUpClass()
		cls.server_url = cls.live_server_url

	@classmethod
	def tearDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, str):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(str, [row.text for row in rows])
