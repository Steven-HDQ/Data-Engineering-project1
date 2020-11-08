import unittest
import os
import requests
import re

class FlaskTests(unittest.TestCase):
	
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		self.text=""
		pass
		
	def test_1_index(self):
		responce = requests.get('http://localhost:5000')
		self.assertEqual(responce.status_code, 200)

	def test_2_test_text(self):
		params = {
			'text': self.text
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(re.findall(r'<H3>(.*)</H3>',responce.text)[0], "")

	def test_3_test_text(self):
		params = {
			'text': "I hate you"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(re.findall(r'<H3>(.*)</H3>',responce.text)[0], "Result: Negative")
	
	def test_4_test_text(self):
		params = {
			'text': "I like you"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(re.findall(r'<H3>(.*)</H3>',responce.text)[0], "Result: Positive")

	def test_5_test_text(self):
		params = {
			'text': "I don't know"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual(re.findall(r'<H3>(.*)</H3>',responce.text)[0], "Result: Neutral")
		
		
if __name__ == '__main__':
	unittest.main()		




