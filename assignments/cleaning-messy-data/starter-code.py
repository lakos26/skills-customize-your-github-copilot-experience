import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    cleaned.columns = [column.strip().lower().replace(" ", "_") for column in cleaned.columns]

    if "name" in cleaned.columns:
        cleaned["name"] = cleaned["name"].astype("string").str.strip().str.title()

    if "category" in cleaned.columns:
        cleaned["category"] = cleaned["category"].astype("string").str.strip().str.lower()

    if "score" in cleaned.columns:
        cleaned["score"] = pd.to_numeric(cleaned["score"], errors="coerce")
        cleaned["score"] = cleaned["score"].fillna(cleaned["score"].mean())

    cleaned = cleaned.drop_duplicates()
    cleaned = cleaned.fillna("")

    return cleaned


def summarize_data(df: pd.DataFrame) -> None:
    print(df.head())
    if "category" in df.columns:
        print(df["category"].value_counts())


def main() -> None:
    df = load_data("data.csv")
    cleaned = clean_data(df)
    summarize_data(cleaned)
    cleaned.to_csv("cleaned_data.csv", index=False)


if __name__ == "__main__":
    main()