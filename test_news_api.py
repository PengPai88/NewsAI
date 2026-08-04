import unittest
import requests
from unittest.mock import patch
from news_api import NewsAPIClient


class TestNewsAPIClient(unittest.TestCase):

    @patch("news_api.requests.get")
    def test_fetch_news_success(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "status": "ok",
            "articles": [
                {"title": "News One"},
                {"title": "News Two"}
            ]
        }

        client = NewsAPIClient()
        result = client.fetch_top_headlines()

        self.assertEqual(len(result), 2)

    @patch("news_api.requests.get")
    def test_fetch_news_empty(self, mock_get):

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "status": "ok",
            "articles": []
        }

        client = NewsAPIClient()
        result = client.fetch_top_headlines()

        self.assertEqual(result, [])

    @patch("news_api.requests.get")
    def test_network_error(self, mock_get):

        mock_get.side_effect = requests.exceptions.RequestException(
            "Network Error"
        )

        client = NewsAPIClient()
        result = client.fetch_top_headlines()

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()