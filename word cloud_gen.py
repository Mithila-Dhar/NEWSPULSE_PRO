from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("cleaned_news.csv")

text = " ".join(df['processed_text'])

wc = WordCloud(width=800, height=400, background_color='black').generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()
