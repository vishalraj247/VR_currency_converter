import unittest
from unittest.mock import patch
from api import get_url
from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import round_rate, reverse_rate, format_output

class TestAppFunctions(unittest.TestCase):

    def test_get_url(self):
        """Test if the get_url function correctly fetches data from an API endpoint."""
        url = "https://www.frankfurter.app/currencies"
        status_code, response_text = get_url(url)
        self.assertEqual(status_code, 200)
        self.assertIn("USD", response_text)

    def test_round_rate(self):
        """Test the rounding functionality of rates to four decimal places."""
        self.assertEqual(round_rate(1.23567), 1.2357)
        self.assertEqual(round_rate(1.2), 1.2000)
        self.assertEqual(round_rate(0), 0)

    def test_reverse_rate(self):
        """Test the calculation of the inverse of a given rate."""
        self.assertEqual(reverse_rate(2), 0.5)
        self.assertEqual(reverse_rate(0), 0)
        self.assertEqual(reverse_rate(0.5), 2)

    def test_format_output(self):
        """Test the proper formatting of currency conversion output."""
        self.assertEqual(
            format_output("2023-09-24", "USD", "EUR", 0.8900, 100.00),
            "The conversion rate on 2023-09-24 from USD to EUR was 0.8900. \nSo 100.00 in USD correspond to 89.00 in EUR. The inverse rate was 1.1236."
        )

    @patch('frankfurter.get_url', return_value=(200, '{"USD":"United States Dollar","EUR":"Euro"}'))
    def test_get_currencies_list(self, mock_get):
        """Test the retrieval of the list of available currencies."""
        result = get_currencies_list()
        expected_result = ['USD', 'EUR']
        self.assertEqual(result, expected_result)

    @patch("api.get_url")
    def test_get_latest_rates(self, mock_get):
        """Test the retrieval of the latest exchange rates for specified currencies."""
        mock_response = """
        {
            "date": "2023-09-22",
            "rates": {"USD": 106.47}
        }
        """
        mock_get.return_value = (200, mock_response)
        date, rate = get_latest_rates("EUR", "USD")
        self.assertEqual(date, "2023-09-22")
        self.assertEqual(rate, 106.47)

    @patch("api.get_url")
    def test_get_historical_rate(self, mock_get):
        """Test the retrieval of historical exchange rates for a specific date and currencies."""
        mock_response = """
        {
            "date": "2023-09-22",
            "rates": {"USD": 106.47}
        }
        """
        mock_get.return_value = (200, mock_response)
        rate = get_historical_rate("EUR", "USD", "2023-09-22")
        self.assertEqual(rate, 106.47)

if __name__ == '__main__':
    unittest.main()