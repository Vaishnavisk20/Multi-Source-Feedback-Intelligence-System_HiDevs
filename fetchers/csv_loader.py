import pandas as pd

def load_survey_csv(file_path):

    try:

        df = pd.read_csv(file_path)

        if "feedback" in df.columns:
            df = df.rename(columns={"feedback":"review"})

        df["source"] = "Survey"
        df["date"] = None
        df["rating"] = None

        return df[["source","review","rating","date"]]

    except Exception as e:

        print("CSV Load Error:", e)

        return pd.DataFrame(columns=["source","review","rating","date"])