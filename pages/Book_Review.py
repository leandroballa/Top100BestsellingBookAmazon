#################################################
#                                               #
#               Display the reviews             #
#           based on a filter for each          #
#                       title.                  #
#                                               #
#################################################
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Book Review")

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100 = pd.read_csv("datasets/Top-100 Trending Books.csv")

books = df_top100["book title"].unique()
book = st.sidebar.selectbox("Books", books)

df_book_f = df_top100[df_top100["book title"] == book]
df_review_f = df_reviews[df_reviews["book name"] == book]

df_title = df_book_f["book title"].iloc[0]
df_genre = df_book_f["genre"].iloc[0]
df_price = f"${df_book_f['book price'].iloc[0]}"
df_rating = df_book_f["rating"].iloc[0]
df_year = df_book_f["year of publication"].iloc[0]

st.title(df_title)
st.subheader(df_genre)

col1, col2, col3 = st.columns(3)
col1.metric("Price", df_price)
col2.metric("Rating", df_rating)
col3.metric("Year of Publication", df_year)

st.divider()

for row in df_review_f.values:
    message = st.chat_message(f"{(row[4])}")
    message.write(f"**{row[2]}**")
    message.write(row[5])