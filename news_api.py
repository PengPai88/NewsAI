# NewsAI Iteration1 | Get daily news quickly (Real NewsAPI data)
import requests

API_KEY = "efe03c4e2220470dbfd22810b904402b"

def get_daily_top_news():
   
    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=4&apiKey={API_KEY}"
    res = requests.get(url)
    data = res.json()

    print("======== NewsAI | Daily Global Top News ========")
    if data["status"] == "ok":
        for idx, article in enumerate(data["articles"], start=1):
            news_title = article["title"]
            print(f"{idx}. {news_title}")
    else:
        print("Failed to fetch news, API quota exhausted temporarily")

if __name__ == "__main__":
    get_daily_top_news()
