import requests
import pandas as pd

api_key = "YOUR_API_KEY"

url = f"http://api.mediastack.com/v1/news?access_key={api_key}&limit=100"

response = requests.get(url)
data = response.json()

articles = data.get("data", [])

df = pd.DataFrame(articles)
df.to_csv("news_data.csv", index=False)

print("Data collected successfully!")
