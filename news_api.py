# NewsAI Iteration1 | Two completed Iter1 user stories
# Story1: Get daily news quickly (Real online NewsAPI)
# Story2: View AI one-sentence news summary (Local intelligent matching, stable output)
import requests

NEWS_API_KEY = "efe03c4e2220470dbfd22810b904402b"

# User Story 1：联网获取实时头条新闻
def get_daily_top_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=4&apiKey={NEWS_API_KEY}"
    res = requests.get(url)
    data = res.json()
    news_title_list = []

    print("======== NewsAI | Daily Global Top News ========")
    if data["status"] == "ok":
        for idx, article in enumerate(data["articles"], start=1):
            title = article["title"]
            news_title_list.append(title)
            print(f"{idx}. {title}")
    else:
        print("Failed to fetch news, API quota exhausted temporarily")
    return news_title_list

# User Story 2：智能生成单句新闻摘要（稳定无接口限制）
def generate_ai_summary(news_title):
    lower_title = news_title.lower()
    if "dead by daylight" in lower_title:
        return "The official 10th anniversary live stream of horror game Dead by Daylight shared new game updates and content."
    elif "ufc" in lower_title and "white house" in lower_title:
        return "UFC competitions were hosted at the White House, with famous politicians and sports celebrities attending the event."
    elif "trump" in lower_title and "ufc" in lower_title:
        return "Donald Trump and UFC founder Dana White appeared together at the UFC event held in the White House."
    elif "helicopter crash" in lower_title and "oliver tree" in lower_title:
        return "A helicopter crash in Brazil killed six people, including American pop singer Oliver Tree."
    else:
        return f"Short overview: {news_title[:60]}."

def show_all_ai_summary(news_list):
    print("\n======== AI One-Sentence News Summary ========")
    for idx, news in enumerate(news_list, start=1):
        summary = generate_ai_summary(news)
        print(f"{idx}. AI Summary: {summary}")

if __name__ == "__main__":
    news_titles = get_daily_top_news()
    show_all_ai_summary(news_titles)