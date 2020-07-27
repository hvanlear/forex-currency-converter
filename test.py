from unittest import TestCase
from app import app


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):

        with self.client:
            response = self.client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(
                '<label for="fromCurrency">Converting From</label>', html)

    def test_conversion(self):

        with self.client:
            response = self.client.post(
                '/convert', data={'fromCurrency': 'USD', 'toCurrency': 'USD'})
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<p>result: US$ 1.0</p>', html)

    def flash_error(self):

        with self.client:
            expected_flash_message = 'zzzz is an invalid currency code'
            response = self.client.post(
                '/convert', data={'fromCurrency': 'zzzz', 'toCurrency': 'USD'})

            self.assertEqual(response.status_code, 200)
            assert expected_flash_message in response.data
