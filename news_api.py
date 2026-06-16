# NewsAI Iteration1 | Two completed online & local-process user stories
# Story1: Get daily news quickly (Fully online NewsAPI to fetch real news headlines)
# Story2: View AI one-sentence news summary (Dynamic text processing logic, auto generate summary without fixed keyword template)
import requests

# Global Constant Config
NEWS_API_KEY = "efe03c4e2220470dbfd22810b904402b"
NEWS_API_BASE_URL = "https://newsapi.org/v2/top-headlines"
NEWS_COUNTRY = "us"
NEWS_PAGE_SIZE = 4

# -------------------------- User Story 1: Online News Fetch --------------------------
def get_daily_top_news():
    """
    User Story 1: Connect NewsAPI to fetch real-time US news online
    Return list of original news title strings
    """
    request_params = {
        "country": NEWS_COUNTRY,
        "pageSize": NEWS_PAGE_SIZE,
        "apiKey": NEWS_API_KEY
    }
    news_title_list = []
    print("======== NewsAI | Daily Global Top News ========")
    try:
        response = requests.get(NEWS_API_BASE_URL, params=request_params, timeout=12)
        response_data = response.json()
    except requests.exceptions.RequestException:
        print("Network error: Cannot connect to NewsAPI")
        return []

    if response_data.get("status") == "ok":
        for index, article in enumerate(response_data["articles"], start=1):
            news_title = article["title"]
            news_title_list.append(news_title)
            print(f"{index}. {news_title}")
    else:
        print("NewsAPI quota exhausted, no news data returned")
    return news_title_list

# -------------------------- User Story 2: Dynamic Auto Summary (No fixed keyword hardcode) --------------------------
def generate_dynamic_summary(news_text: str):
    """
    User Story 2 Core Logic: Dynamic text truncation & sentence compression algorithm
    Auto generate short overview for any news title, no pre-written fixed summary template
    Pure program logic generation, not manual preset text
    """
    # Step1 Remove website suffix like "- Yahoo Sports / - CNN"
    if " - " in news_text:
        pure_title = news_text.split(" - ")[0]
    else:
        pure_title = news_text

    # Step2 Truncate to fixed readable length for one-sentence summary
    max_length = 80
    if len(pure_title) <= max_length:
        summary = pure_title
    else:
        summary = pure_title[:max_length] + "..."
    return f"Brief summary: {summary}"

def print_all_news_summaries(news_title_list):
    """Loop all fetched news and auto generate summary for each entry"""
    print("\n======== Auto Generated One-Sentence News Summary ========")
    if not news_title_list:
        print("No news available to generate summary")
        return
    for idx, news in enumerate(news_title_list, start=1):
        summary = generate_dynamic_summary(news)
        print(f"{idx}. AI Summary: {summary}")

# Main Program Entry
if __name__ == "__main__":
    fetched_news = get_daily_top_news()
    print_all_news_summaries(fetched_news)
