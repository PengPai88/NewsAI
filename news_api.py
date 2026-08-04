import requests
from typing import List, Dict

# ==========================
# Global Configuration
# ==========================

NEWS_API_KEY = "efe03c4e2220470dbfd22810b904402b"
NEWS_API_BASE_URL = "https://newsapi.org/v2/top-headlines"
NEWS_COUNTRY = "us"
NEWS_PAGE_SIZE = 4
MAX_SUMMARY_LENGTH = 80


# ==========================
# News API Client
# ==========================

class NewsAPIClient:
    """
    Responsible for retrieving news from NewsAPI.
    """

    def fetch_top_headlines(self) -> List[Dict]:

        params = {
            "country": NEWS_COUNTRY,
            "pageSize": NEWS_PAGE_SIZE,
            "apiKey": NEWS_API_KEY
        }

        try:
            response = requests.get(
                NEWS_API_BASE_URL,
                params=params,
                timeout=12
            )

            response.raise_for_status()

            data = response.json()

            if data.get("status") != "ok":
                return []

            return data.get("articles", [])

        except requests.exceptions.RequestException:
            return []


# ==========================
# Summary Processor
# ==========================

class TextSummaryProcessor:
    """
    Responsible for generating AI-style summaries.
    """

    @staticmethod
    def generate_summary(news_title: str) -> str:

        if not news_title:
            return "Brief summary: "

        # Remove source name
        pure_title = news_title.split(" - ")[0]

        # Limit summary length
        if len(pure_title) > MAX_SUMMARY_LENGTH:
            pure_title = pure_title[:MAX_SUMMARY_LENGTH] + "..."

        return f"Brief summary: {pure_title}"


# ==========================
# Console Printer
# ==========================

class ConsolePrinter:
    """
    Responsible only for displaying information.
    """

    @staticmethod
    def print_news(articles: List[Dict]):

        print("======== NewsAI | Daily Global Top News ========")

        if not articles:
            print("No news available")
            return

        for index, article in enumerate(articles, start=1):
            print(f"{index}. {article['title']}")

    @staticmethod
    def print_summaries(articles: List[Dict]):

        print("\n======== Auto Generated One-Sentence News Summary ========")

        if not articles:
            print("No news available to generate summary")
            return

        for index, article in enumerate(articles, start=1):

            summary = TextSummaryProcessor.generate_summary(
                article["title"]
            )

            print(f"{index}. {summary}")


# ==========================
# Main Application
# ==========================

class NewsApplication:
    """
    Main workflow controller.
    """

    def __init__(self):

        self.news_client = NewsAPIClient()

    def run(self):

        articles = self.news_client.fetch_top_headlines()

        ConsolePrinter.print_news(articles)

        ConsolePrinter.print_summaries(articles)


# ==========================
# Program Entry
# ==========================

if __name__ == "__main__":

    app = NewsApplication()


    app.run()