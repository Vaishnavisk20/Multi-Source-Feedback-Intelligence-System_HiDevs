import feedparser
import pandas as pd

def fetch_app_store_reviews(rss_url):

    try:

        feed = feedparser.parse(rss_url)

        data = []

        for entry in feed.entries:

            review = entry.get("title","")
            date = entry.get("published",None)

            data.append({
                "source": "App Store",
                "review": review,
                "rating": None,
                "date": date
            })

        return pd.DataFrame(data)

    except Exception as e:

        print("App Store Fetch Error:", e)

        return pd.DataFrame(columns=["source","review","rating","date"])