import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import pickle
from migrate import db_execute_fetch

# model codes


st.set_page_config(
    page_title="Telecom Dataset Analysis", layout="wide")


def loadData():
    query = "select * from Customer_Satisfaction"
    df = db_execute_fetch(query, dbName="Telecom", rdf=True)
    return df


# def selectHashTag():
#     df = loadData()
#     hashTags = st.multiselect(
#         "choose combaniation of hashtags", list(df['hashtags'].unique()))
#     if hashTags:
#         df = df[np.isin(df, hashTags).any(axis=1)]
#         st.write(df)


# def selectLocAndAuth():
#     df = loadData()
#     location = st.multiselect(
#         "choose Location of tweets", list(df['place'].unique()))
#     lang = st.multiselect("choose Language of tweets",
#                           list(df['lang'].unique()))

#     if location and not lang:
#         df = df[np.isin(df, location).any(axis=1)]
#         st.write(df)
#     elif lang and not location:
#         df = df[np.isin(df, lang).any(axis=1)]
#         st.write(df)
#     elif lang and location:
#         location.extend(lang)
#         df = df[np.isin(df, location).any(axis=1)]
#         st.write(df)
#     else:
#         st.write(df)


def barChart(data, title, X, Y):
    title = title.title()
    st.title(f'{title} Chart')
    msgChart = (alt.Chart(data).mark_bar().encode(alt.X(f"{X}:N", sort=alt.EncodingSortField(field=f"{Y}", op="values",
                order='ascending')), y=f"{Y}:Q"))
    st.altair_chart(msgChart, use_container_width=True)



fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    st.title("Data Display")
    st.write(loadData())


# #sentiment compute
# with fig_col1:
#     st.title("Customer Satisfaction Analysis")

#     # title = st.text_input('Insert sentence to compute sentiment', '') 
    
#     model = st.multiselect(
#         "choose from the given models", models)
#     if model!=[]:
#         model_index = models.index(model[0])
#         result = compute_sentiment(n = model_index,sentence=title)
#         res = ''
#         if result==0:
#             res = 'Negative'
#         elif result ==1:
#             res = 'Positive'
            
#         st.write('The sentence is:', res)
    
# with fig_col2:
#     st.title("Data Visualizations")
#     selectHashTag()
#     st.markdown("<p style='padding:10px; background-color:#000000;color:#00ECB9;font-size:16px;border-radius:10px;'>Section Break</p>", unsafe_allow_html=True)
#     selectLocAndAuth()
# wordCloud()
# with st.expander("Show More Graphs"):
#     stBarChart()
#     langPie()









