from google_play_scraper import reviews
import pandas as pd

def fetch_google_reviews(app_id):

    try:

        result, _ = reviews(
            app_id,
            lang="en",
            country="us",
            count=100
        )

        data = []

        for r in result:

            data.append({
                "source": "Google Play",
                "review": r["content"],
                "rating": r["score"],
                "date": r["at"]
            })

        return pd.DataFrame(data)

    except Exception as e:

        print("Google Play Fetch Error:", e)

        return pd.DataFrame(columns=["source","review","rating","date"])