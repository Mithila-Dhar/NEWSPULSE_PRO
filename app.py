import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NewsPulse", layout="wide")

st.title("🌍 NewsPulse - Global News Trend Analyzer")

# Load Data
news_data = pd.read_csv("cleaned_news.csv")

# Metrics
col1, col2 = st.columns(2)
col1.metric("Total Articles", len(news_data))
col2.metric("Unique Sources", news_data['source'].nunique())

# Sentiment Chart
sentiment_counts = news_data['sentiment_label'].value_counts()
fig = px.pie(values=sentiment_counts.values,
             names=sentiment_counts.index,
             title="Sentiment Distribution")
st.plotly_chart(fig)

# Trending Words
trend_df = news_data['processed_text'].str.split().explode().value_counts().head(5).reset_index()
trend_df.columns = ["Word", "Frequency"]

fig2 = px.bar(trend_df, x="Frequency", y="Word", orientation="h",
              title="Top Trending Words")
st.plotly_chart(fig2)
