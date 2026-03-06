from textblob import TextBlob

def analyze_sentiment(text):

    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0.2:
        sentiment = "Positive"
    elif polarity < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    confidence = abs(polarity)

    return sentiment, round(confidence,2)