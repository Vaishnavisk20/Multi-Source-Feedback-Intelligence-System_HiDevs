from collections import Counter
import re

def detect_issues(df):

    negative = df[df["sentiment"]=="Negative"]

    words = []

    for review in negative["review"]:

        tokens = re.findall(r'\b\w+\b', str(review).lower())

        words.extend(tokens)

    common = Counter(words).most_common(10)

    return common