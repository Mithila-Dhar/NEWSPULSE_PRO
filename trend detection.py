import pandas as pd
from collections import Counter

df = pd.read_csv("cleaned_news.csv")

all_words = " ".join(df['processed_text']).split()

word_freq = Counter(all_words)

top_words = word_freq.most_common(10)

for word, freq in top_words:
    print(word, freq)
