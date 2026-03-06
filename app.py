import streamlit as st
import pandas as pd

from fetchers.google_play_fetcher import fetch_google_reviews
from fetchers.app_store_fetcher import fetch_app_store_reviews
from fetchers.csv_loader import load_survey_csv

from analysis.sentiment_analysis import analyze_sentiment
from analysis.trend_analysis import calculate_trend
from analysis.issue_detection import detect_issues

from reports.pdf_report import generate_pdf


st.title("Feedback Intelligence System")

app_id = st.text_input("Google Play App ID", "com.instagram.android")

rss_url = st.text_input(
    "App Store RSS",
    "https://itunes.apple.com/rss/customerreviews/page=1/id=389801252/sortby=mostrecent/xml"
)


if st.button("Fetch Feedback"):

    # Fetch data from sources
    google = fetch_google_reviews(app_id)
    appstore = fetch_app_store_reviews(rss_url)
    survey = load_survey_csv("data/survey_feedback.csv")

    frames = [google, appstore, survey]

    clean_frames = []

    for f in frames:
        if isinstance(f, pd.DataFrame) and not f.empty:

            # remove columns that contain only NaN
            f = f.dropna(axis=1, how="all")

            # remove rows that contain only NaN
            f = f.dropna(how="all")

            if not f.empty:
                clean_frames.append(f)

    if clean_frames:
        df = pd.concat(clean_frames, ignore_index=True)
    else:
        st.warning("No feedback data available from sources.")
        st.stop()

    # Sentiment analysis
    sentiments = []
    confidence = []

    for review in df["review"]:

        s, c = analyze_sentiment(review)

        sentiments.append(s)
        confidence.append(c)

    df["sentiment"] = sentiments
    df["confidence"] = confidence

    # Show feedback table
    st.subheader("Feedback Data")
    st.dataframe(df)

    # Sentiment distribution
    st.subheader("Sentiment Distribution")
    st.bar_chart(df["sentiment"].value_counts())

    # Trend chart
    st.subheader("Sentiment Trend")
    trend = calculate_trend(df)

    if trend is not None and not trend.empty:
        st.line_chart(trend)

    # Issue detection
    st.subheader("Top Issues Detected")
    issues = detect_issues(df)

    st.write(issues)

    # Summary for PDF
    summary = [
        f"Total Reviews: {len(df)}",
        f"Positive Reviews: {sum(df.sentiment == 'Positive')}",
        f"Negative Reviews: {sum(df.sentiment == 'Negative')}",
        f"Neutral Reviews: {sum(df.sentiment == 'Neutral')}"
    ]

    # PDF report
    if st.button("Generate PDF Report"):

        file = generate_pdf(summary)

        with open(file, "rb") as f:
            st.download_button(
                label="Download PDF Report",
                data=f,
                file_name=file,
                mime="application/pdf"
            )