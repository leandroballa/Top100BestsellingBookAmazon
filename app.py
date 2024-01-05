#################################################
#                                               #
#               Main Page                       #
#       Shows Top 100 Bestselling Book          #
#   Reviews on Amazon and you can filter        #
#   by price. Also, it is possible to see       #
#   the number of books published by year       #
#       nd the number of books by price         #
#                                               #
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
df_books = df_books.drop("url", 1)

df_books

fig = px.bar(df_books["year of publication"].value_counts(), title="Amount of Book Publicated by Year")
fig2 = px.histogram(df_books["book price"], title="Amount of Books by Price", text_auto=True)

col1, col2 = st.columns(2)

col1.plotly_chart(fig, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)
