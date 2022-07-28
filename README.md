# Countries data app

App for building a table with data from countries and save it to a json file and sqlite database. It retrieves data from [Rest Countries API](https://restcountries.com/) and builds a pandas dataframe. Each row contains country region, country name, an encrypted version of country language in SHA1 and time elapsed in building row.


## Installation 🔧

Clone the repository in a your work folder.

## Configuration

### Create a virtual environment
```
python -m venv .venv
```
### Activate virtul environment

#### Windows
```
.venv\Scripts\activate
```
#### Linux
```
source .venv/bin/activate
```
### Download all packages required
```
pip install -r requirements.txt
```
### Create an environment file

You must create a .env file for project configuration. It must contain following variables:

```


```

## Running tests
### Test all app modules
```
python -m unittest tests/test.py -v
```

## Run app
```
python run.py
```
