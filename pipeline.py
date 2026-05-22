import pandas as pd  # type: ignore
from database import insert_data, get_connection
from logic import Patient, Doctor


# Extract
def extract():
    print("Extracting.....")
    return pd.read_csv("data.csv")


# Transform
def transform(df):
    print("Transforming.....")

    df = df.drop_duplicates()
    df = df.fillna("Unknown")

    return df


# Load
def load(conn,df):
    print("Loading.....")
    insert_data(conn,df)


# Main Pipeline
if __name__ == "__main__":
    conn = get_connection()
    df = extract()
    df = transform(df)
    load(conn,df)

    print("ETL Completed.....!")
