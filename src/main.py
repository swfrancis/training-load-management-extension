import requests
import pandas as pd

ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"
AUTH_URL = "https://www.strava.com/oauth/token"

CLIENT_ID = "151103"
ACCESS_TOKEN = "cdf663d5f9ca9b53dd38d0c2b3ed8f2bdd684f99"
REFRESH_TOKEN: "5d8c57a153c2755dcc3f7f48e98098af17f31203"

header = {"Authorization": "Bearer " + ACCESS_TOKEN}
param = {"per_page": 200, "page": 1}
response = requests.get(ACTIVITIES_URL, headers=header, params=param).json()

activities = pd.json_normalize(response)
print(activities)
