import unittest
from unittest.mock import patch

from news_api import NewsApplication


class TestNewsApplication(unittest.TestCase):

    @patch("news_api.ConsolePrinter.print_news")
    @patch("news_api.ConsolePrinter.print_summaries")
    @patch("news_api.NewsAPIClient.fetch_top_headlines")
    def test_run(
            self,
            mock_fetch,
            mock_print_summaries,
            mock_print_news):

        mock_fetch.return_value = [
            {"title": "News One"},
            {"title": "News Two"}
        ]

        app = NewsApplication()

        app.run()

        mock_fetch.assert_called_once()

        mock_print_news.assert_called_once()

        mock_print_summaries.assert_called_once()


if __name__ == "__main__":
    unittest.main()