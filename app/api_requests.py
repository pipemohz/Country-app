import requests
from settings import URL_API_REST_COUNTRIES


def request_to_rest_countries() -> requests.Response:
    """
    Makes a request to Rest countries API to get data of all countries stored.
    ### Returns
    `request.Response`
        Response object with data retrived from API response.
    """

    params = {
        "fields": "name,languages,region"
    }

    response = requests.get(url=URL_API_REST_COUNTRIES, params=params)

    return response
