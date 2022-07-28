from .api_requests import request_to_rest_countries
from .process_data import build_dataframe, show_info, create_json, create_sqlite_db


def main():
    # Get countries data from API
    response = request_to_rest_countries()
    # Build dataframe with data
    if response.ok:
        df = build_dataframe(response.json())
        # Show dataframe's info
        show_info(df)
        # Create a json file with df data
        create_json(df)
        # Create a sqlite database with df
        create_sqlite_db(df)
