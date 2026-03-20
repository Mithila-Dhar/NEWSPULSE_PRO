import pandas as pd
import re
from nltk.corpus import stopwords

df = pd.read_csv("news_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Remove nulls
df = df.dropna(subset=['title'])

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words and len(w) > 2]
    return " ".join(words)

df['processed_text'] = df['title'].apply(clean_text)

df.to_csv("cleaned_news.csv", index=False)

print("Data cleaned successfully!")
