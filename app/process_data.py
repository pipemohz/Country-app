import os
import pandas as pd
import hashlib
import time
from settings import BASE_DIR
from sqlalchemy import create_engine


def build_dataframe(data: dict) -> pd.DataFrame:
    """
    Builds a pandas `dataframe` from `data` dictionary. 
    ### Parameters 
    `data: dict` 
        Data dictionary with response format of Rest countries API. Check response example in 
        https://restcountries.com/#api-endpoints-v2-response-example.

    ### Returns
    `pandas.Dataframe` 
    """

    countries_names = []
    languages = []
    regions = []
    times = []

    for record in data:
        tic = time.perf_counter()
        countries_names.append(record["name"]["common"])
        if list(record["languages"].values()):
            languages.append(hashlib.sha1(list(record["languages"].values())[
                0].encode('utf8')).hexdigest())
        else:
            languages.append("No language")
        regions.append(record["region"])
        times.append(float("{:.4f}".format(
            (time.perf_counter() - tic) * 1000)))

    # Build dict with keys as Columns and lists as values
    countries = {
        "Region": regions,
        "Name": countries_names,
        "Language": languages,
        "Time(ms)": times
    }

    # Build dataframe from dict
    df = pd.DataFrame.from_dict(countries)

    return df


def show_info(df: pd.DataFrame):
    """
    Prints stats `dataframe`'s time column. 
    ### Parameters 
    `df: pd.Dataframe`
        Pandas dataframe. It must have a column called "Time(ms).
    """

    if not df.empty and 'Time(ms)' in df.columns:
        # Print total time
        print(f"Total time: {df['Time(ms)'].sum()} ms")
        # Print Average time
        print(f"Average time: {df['Time(ms)'].mean()} ms")
        # Print Minimum time
        print(f"Minimum Time: {df['Time(ms)'].min()} ms")
        # Print Maximum time
        print(f"Maximum Time: {df['Time(ms)'].max()} ms")

    else:
        raise KeyError("Column 'Time(ms) does not exist.")


def create_json(df: pd.DataFrame, path=BASE_DIR, filename="data.json"):
    """
    Creates a json file from df in `path` with name `filename`.
    ### Parameters
    `df: pd.Dataframe`
        Pandas dataframe. 

    `path: str`
        Path to save json file. By default is set to app's root folder.

    `filename: str`
        Name of json file. By default is set to "data.json".

    """
    df.to_json(os.path.join(path, filename))


def create_sqlite_db(df: pd.DataFrame, filename="data.db"):
    """
    Creates a sqlite database from df in app's root folder.
    ### Parameters
    `filename: str`
        Name of json file. By default is set to "data.json". 
    """

    engine = create_engine(f'sqlite:///{filename}', echo=False)

    with engine.begin() as conn:
        df.to_sql('countries', con=conn, if_exists='append')
