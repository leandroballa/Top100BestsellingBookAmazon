import streamlit as st
import pandas as pd
import plotly.express as px 

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100 = pd.read_csv("datasets/Top-100 Trending Books.csv")

price_max = df_top100["book price"].max()
price_min = df_top100["book price"].min()
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

df_books = df_top100[df_top100["book price"] <= max_price]

df_books

fig = px.bar(df_books["year of publication"].value_counts())

st.plotly_chart(fig)
