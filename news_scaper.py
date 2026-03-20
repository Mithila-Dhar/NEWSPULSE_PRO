import requests
import pandas as pd

def fetch_news(api_key):
    url = f"http://api.mediastack.com/v1/news?access_key={api_key}&limit=100"
    data = requests.get(url).json()
    return pd.DataFrame(data.get("data", []))
