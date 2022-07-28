import os
from dotenv import load_dotenv

load_dotenv()

# Project settings
BASE_DIR = os.path.dirname(__file__)

# Rest countries API settings
URL_API_REST_COUNTRIES = os.environ.get('URL_API_REST_COUNTRIES')
