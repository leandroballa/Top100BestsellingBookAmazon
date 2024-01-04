#################################################
#                                               #
#               Main Page                       #
#       Shows Book when you can filter          #
#       by price. Also it is possible           #
#       see the amount of books published       #
#       by year and the amount of book by       #
#       price                                   #
#################################################
import streamlit as st
import pandas as pd
import plotly.express as px 

st.set_page_config(layout="wide", page_title="Book List")

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100 = pd.read_csv("datasets/Top-100 Trending Books.csv")

price_max = df_top100["book price"].max()
price_min = df_top100["book price"].min()
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

df_books = df_top100[df_top100["book price"] <= max_price]

with st.container():
    df_books

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)
