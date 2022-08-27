import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import pickle
from migrate import db_execute_fetch
from EDA import *
import os

pwd = os.getcwd()

st.set_page_config(
    page_title="Telecom Dataset Analysis", layout="wide")

    
def barChart(data, title, X, Y):
    title = title.title()
    st.title(f'{title} Chart')
    msgChart = (alt.Chart(data).mark_bar().encode(alt.X(f"{X}:N", sort=alt.EncodingSortField(field=f"{Y}", op="values",
                order='ascending')), y=f"{Y}:Q"))
    st.altair_chart(msgChart, use_container_width=True)
    
df_customer = pd.read_pickle(pwd + '/data/df_customer.pkl')
df_experience = pd.read_pickle(pwd+ '/data/df_experience.pkl')
df_engagement = pd.read_pickle(pwd + '/data/df_engagement.pkl')
df_sat = pd.read_pickle(pwd+'/data/df_sat.pkl')


def countPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x = "total_session", data = df_customer)
    st.pyplot(fig)
    


def loadData():
    query = "select * from Customer_Satisfaction"
    df = db_execute_fetch(query, dbName="Telecom", rdf=True)
    return df

def main_page():
    # st.markdown("# Customer Experience ")
    st.sidebar.markdown("# Main page ")

    col1, col2 = st.columns(2)

    with col1:
        st.title('Top 10 Customers with Youtube Download')
        st.table(df_customer.iloc[df_customer.Youtube_DL.nlargest(10).index][['ID','Youtube_DL']])
    with col2:
        st.title('Top 10 Customers with Netflix Download')
        st.table(df_customer.iloc[df_customer.Netflix_DL.nlargest(10).index][['ID','Netflix_DL']])
    # st.section()

    col3,col4 = st.columns(2)
    with col3:
        st.title("Total Data Distributions number of sessions")
        countPlot()
    with col4:
        st.title('Top 3 used applications per Download')
        st.table(df_customer[df_customer.columns[3:9]].sum().nlargest(3))



# def page2():
#     st.markdown("# Page 2 ❄️")
#     st.sidebar.markdown("# Customer Experience ❄️")


def page2():
    st.markdown("# Page 2 ")
    st.sidebar.markdown("# Customer Engagement ")

    
    col1,col2 = st.columns(2)
    with col1:
        
        st.title('Top 10 customers with hign session frequency')
        st.table(df_engagement.iloc[df_engagement.total_session.nlargest(10).index])

    with col2:
        st.title("Top 10 customers with longer session duration")
        st.table(df_engagement.iloc[df_engagement.session_duration.nlargest(10).index])
    
    col11,col12 = st.columns(2)
     
    with col11:
        # Top 10 customers with largest session total trafic (Download)
        st.title('Top 10 customers with largest session total trafic')
        st.table(df_engagement.iloc[df_engagement.Total_DL.nlargest(10).index])
    with col12:
        # Top 10 customers with largest session total trafic (Upload)
        st.title('Top 10 customers with largest session total trafic')
        st.table(df_engagement.iloc[df_engagement.Total_UL.nlargest(10).index])
        
    cola,colb,colc = st.columns(3)
    with cola:
        # Top 10 engaged users per application
        st.title('Top 10 Engaged users per application')
        st.table(df_customer.iloc[df_customer.Youtube_DL.nlargest(10).index][['ID','Youtube_DL']])
    with colb:
        st.title('top 3 most used applications / Per Download')
        st.table(df_customer[df_customer.columns[3:9]].sum().nlargest(3))
    with colc:
        st.title('top 3 most used applications / Per Upload')
        st.table(df_customer[df_customer.columns[11:17]].sum().nlargest(3))
        
        
        
        
        
def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Customer Satisfaction 🎉")
    cola,colb= st.columns(2)
    with cola:
        st.title('Top max values')
        st.table(df_experience.iloc[df_experience.Avg_TCP_DL.nlargest(10).index][['ID','Avg_TCP_DL']])
    with colb:
        st.title('Top min values')
        st.table(df_experience.iloc[df_experience.Avg_TCP_DL.nsmallest(10).index][['ID','Avg_TCP_DL']])
    with cola:
        # top 10 satisfied
        st.title('Top 10 satisfied customers')
        st.table(df_sat.loc[df_sat.Satisfaction_score.nlargest(10).index])

        

def page4():
    st.markdown("Total Dataset ")
    st.sidebar.markdown("# Page 4 🎉")
    st.title("Data Display")
    st.write(loadData())
    cola,colb = st.columns(2)
    

page_names_to_funcs = {
    "Main Page": main_page,
    "Customer Engagement": page2,
    "Customer Satisfaction": page3,
    "Total Dataset ": page4,
}

selected_page = st.sidebar.selectbox(
    "Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


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
