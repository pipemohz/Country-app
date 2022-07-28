import unittest
from app.api_requests import request_to_rest_countries
from app.process_data import build_dataframe, create_json, create_sqlite_db, show_info
from settings import BASE_DIR
import pandas as pd
import os


class BasicTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        os.remove(os.path.join(BASE_DIR, "data.json"))
        os.remove(os.path.join(BASE_DIR, "data.db"))

    def setUp(self) -> None:
        # return super().setUp()
        self.test_data = [{
            "name": {
                "common": "Greenland",
                "official": "Greenland",
                "nativeName": {
                    "kal": {
                        "official": "Kalaallit Nunaat",
                        "common": "Kalaallit Nunaat"
                    }
                }
            },
            "region": "Americas",
            "languages": {
                "kal": "Greenlandic"
            }
        }]
        self.columns = ["Region", "Name", "Language", "Time(ms)"]
        self.df1 = pd.DataFrame({"Region": ["Americas"], "Name": [
            "Greenland"], "Language": ["Greenlandic"], "Time(ms)": [0.0268]})
        self.df2 = pd.DataFrame({"Region": ["Americas"], "Name": [
            "Greenland"], "Language": ["Greenlandic"], "Time": [0.0268]})

    def tearDown(self) -> None:
        # return super().tearDown()
        pass

    def test_request(self):
        self.assertTrue(request_to_rest_countries().ok)

    def test_build_dataframe(self):
        self.assertIsInstance(build_dataframe(self.test_data), pd.DataFrame)
        self.assertEqual(build_dataframe(
            self.test_data).columns.to_list(), self.columns)

    def test_show_info(self):
        with self.assertRaises(KeyError):
            show_info(self.df2)

    def test_create_json(self):
        create_json(self.df1)
        self.assertTrue(os.path.exists(os.path.join(BASE_DIR, "data.json")))

    def test_create_sqlite_db(self):
        create_sqlite_db(self.df1)
        self.assertTrue(os.path.exists(os.path.join(BASE_DIR, "data.db")))


if __name__ == "__main__":
    unittest.main()
