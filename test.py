from unittest import TestCase
from app import app

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):
    def setUp(self):
        """before calls all Test Method"""
        self.client = app.test_client()
        app.config["TESTING"]=True
        

    def test_get_converted_value(self):
        with app.test_client as client:
            result = client.post('/result',data = {'text-from' : 'INR','text-to' : 'USD','text':'1'})
            html = result.get_data(as_text = True)
            self.assertEqual(result.status_code,200)
            self.assertIn('<html>',html)