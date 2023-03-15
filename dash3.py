import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plost
import datetime as dt
from dateutil.relativedelta import relativedelta


st.set_page_config(layout='wide', initial_sidebar_state='expanded',page_title='Share Price Dashboard')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    
selected2 = option_menu(None, ["ANALYSE", "DATAFRAME", "SHARE PRICE"], 
    icons=['graph-up-arrow', 'clipboard-data', 'bar-chart-line-fill'], 
    menu_icon="cast", default_index=0, orientation="horizontal")


if selected2 =="ANALYSE" :
        
    st.sidebar.header('Dashboard `version 2`')

    st.sidebar.subheader('Donut chart parameter')
    donut_theta = st.sidebar.selectbox('Select data', ('Q1', 'Q2','Q3','Q4'))

    st.sidebar.subheader('line chart parameter')
    time_color = st.sidebar.selectbox('Color by', ('Amazon', 'Apple','Facebook','Google'))

    st.sidebar.subheader('Line chart parameters')
    plot_data = st.sidebar.multiselect('Select data', ['Amazon', 'Apple','Facebook','Google'], ['Amazon', 'Apple','Facebook','Google'])
    plot_height = st.sidebar.slider('Specify plot height', 200, 900, 350)
    
        #row 1
    st.header("SHARE PRICE")
    st.markdown('## Metrics')
    col1, col2, col3,col4= st.columns(4)
    col1.metric("Amazon", "3384.179 ₹", "-0.02%")
    col2.metric("Apple", "179.26 ₹", "0.04%")
    col3.metric("Facebook", "342.29 ₹", "0.01%")
    col4.metric("Google","2930.59 ₹" , "0.04%" )
    
    #row2
    c1, c2 = st.columns((5,4))
    with c1 :
    
        st.markdown("## DATASET")
        df = pd.read_csv("stockprice5.csv")
        st.write(df)
    with c2:
        sto = pd.read_csv("Sto.csv")
    
        st.markdown('## Donut chart')
        st.markdown("#### 2021 Profit & Loss In Percentage")
        plost.donut_chart(
        data=sto,
        theta=donut_theta,
        color='company',
        legend='bottom', 
        use_container_width=True)
    #row4
    stocks = pd.read_csv('stockprice5.csv',parse_dates=['Date'])

    st.line_chart(stocks, x = 'Date', y = plot_data, height = plot_height)

    #row5
    st.header("Scatter Plot")
    c1, c2 = st.columns((4,4))
    with c1 :
        st.markdown("### Apple v/s Facebook")
        fig, ax =plt.subplots()
        ax.scatter(stocks['Apple'],stocks['Facebook'])
        st.pyplot(fig)
    with c2 :
        st.markdown("### Amazon v/s Google")
        fig, ax =plt.subplots()
        ax.scatter(stocks['Amazon'],stocks['Google'])
        st.pyplot(fig)
    
    c1, c2 = st.columns((4,4))
    with c1 :
        st.markdown("### Apple v/s Google")
        fig, ax =plt.subplots()
        ax.scatter(stocks['Apple'],stocks['Google'])
        st.pyplot(fig)
    with c2 :
        st.markdown("### Amazon v/s Facebook")
        fig, ax =plt.subplots()
        ax.scatter(stocks['Amazon'],stocks['Facebook'])
        st.pyplot(fig)    

if selected2 =="DATAFRAME":
    
    st.markdown("## DATASET (2017-2021)")
    
    
   
    df = pd.read_csv("stockprice5.csv")
    st.dataframe(df,4000,500)

if selected2 == "SHARE PRICE" :
    st.sidebar.header('Dashboard `version 2`')
    
    
    plot_height = st.sidebar.slider('Specify plot height', 200, 900, 500)
    plot_data = st.sidebar.multiselect('Select data', ['Amazon', 'Apple','Facebook','Google'], ['Amazon', 'Apple','Facebook','Google'])
    stocks = pd.read_csv('stockprice5.csv',parse_dates=['Date'])
    st.header("Bar Chart")
    st.bar_chart(stocks ,x = 'Date' , y = plot_data ,height = plot_height) 