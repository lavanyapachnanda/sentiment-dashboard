import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("Social Media Sentiment Dashboard")
st.write("Upload your tweet dataset to explore sentiment analysis")

file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:
    df = pd.read_csv(file, header=None)
    df.columns = ['id', 'entity', 'sentiment', 'text']
    df = df.dropna()

    st.subheader("Dataset Preview")
    st.write(df.head())

    st.subheader("Chart 1 — Sentiment Distribution")
    fig1, ax1 = plt.subplots()
    df['sentiment'].value_counts().plot(kind='bar', ax=ax1, color=['green','red','gray','blue'])
    ax1.set_xlabel("Sentiment")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

    st.subheader("Chart 2 — Top 10 Topics")
    fig2, ax2 = plt.subplots(figsize=(10,4))
    df['entity'].value_counts().head(10).plot(kind='bar', ax=ax2, color='steelblue')
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    st.subheader("Chart 3 — Positive Tweets Word Cloud")
    pos_text = ' '.join(df[df['sentiment'] == 'Positive']['text'].astype(str))
    wc = WordCloud(width=800, height=300, background_color='white').generate(pos_text)
    fig3, ax3 = plt.subplots()
    ax3.imshow(wc)
    ax3.axis('off')
    st.pyplot(fig3)