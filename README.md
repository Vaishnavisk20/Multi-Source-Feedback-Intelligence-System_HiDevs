# Multi-Source Feedback Intelligence System

## Overview

The **Multi-Source Feedback Intelligence System** is a Python-based analytics platform designed to collect and analyze user feedback from multiple real-world sources including **Google Play Store reviews**, **Apple App Store RSS feeds**, and **survey CSV files**.

The system performs **sentiment analysis** to classify customer feedback, identifies recurring issues and trends, and provides insights through an **interactive Streamlit dashboard**. It also generates **professional PDF reports** that can be shared with stakeholders or product teams.

---

## Features

* Multi-source feedback integration
* Google Play Store review fetching
* Apple App Store RSS review fetching
* Survey CSV feedback import
* Sentiment analysis with confidence scores
* Trend detection over time
* Automatic issue detection from negative reviews
* Interactive Streamlit dashboard
* Automated PDF report generation

---

## Technology Stack

* Python
* Streamlit
* Pandas
* TextBlob (Sentiment Analysis)
* Google Play Scraper API
* Feedparser (RSS parsing)
* ReportLab (PDF generation)

---

## Project Structure

```
feedback_intelligence_multi_source_hidevs

app.py
requirements.txt
README.md

fetchers/
    google_play_fetcher.py
    app_store_fetcher.py
    csv_loader.py

analysis/
    sentiment_analysis.py
    trend_analysis.py
    issue_detection.py

reports/
    pdf_report.py

data/
    survey_feedback.csv
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/feedback_intelligence_multi_source_hidevs.git
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Download TextBlob Dataset

```
python -m textblob.download_corpora
```

### 4. Run the Application

```
streamlit run app.py
```

---

## Dashboard Capabilities

The Streamlit dashboard provides:

* Aggregated feedback from multiple sources
* Sentiment classification of customer reviews
* Sentiment trend visualization
* Identification of frequently mentioned issues
* Interactive charts and tables for analysis

---

## PDF Report Generation

The system can generate a downloadable **PDF summary report** that includes:

* Total number of reviews analyzed
* Positive / Negative / Neutral sentiment distribution
* Key insights from customer feedback

---

## Demo Video

YouTube Demo Link:
https://youtube.com/shorts/bBPnMFshBd4?feature=share

---

## Author

Vaishnavi SK
