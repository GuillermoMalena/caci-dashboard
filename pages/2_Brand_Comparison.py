import streamlit as st
from annotated_text import annotated_text
import pandas as pd
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
import os

st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)


brand_profiles = ('./sub_brand_profiles')
brand_avgs = ('./brand_means')
    
brands_key_df = pd.read_csv('./brands_key.csv',dtype={'User ID':'string'})
brands_key_list = brands_key_df['User'].drop_duplicates().to_list()

brands_list = [x.lower() for x in brands_key_list]


brands = st.multiselect(
    "Choose which brands you would like to compare directly", brands_list, ["kendricklamar", "drake"]
)

jobs_df = []
ints_df = []
city_df = []
nats_df = []
def get_profile(brand, profile):
    profile = pd.read_csv(os.path.join(brand_profiles,f'{brand}_{profile}.csv'),dtype=str).head(15)
    profile = profile.rename(columns ={f'{brand}_percent':'Percent'})
    profile['Percent'] = profile['Percent'].astype(float).round(2)
    profile['Brand'] = i

    return profile
for i in brands:
    ints = get_profile(i,'interests')
    jobs = get_profile(i,'jobs')
    city = get_profile(i,'city')
    nat = get_profile(i,'nationality')
    ints_df.append(ints)
    jobs_df.append(jobs)
    city_df.append(city)
    nats_df.append(nat)

profiles = ['jobs','interests','nationality','city']
profile_option = st.radio("Choose a profile to analyze the brands for",profiles,1,horizontal=True )

st.subheader(f"Top follower {profile_option}")
total_jobs = pd.concat(jobs_df)
total_ints = pd.concat(ints_df)
total_city= pd.concat(city_df)
total_nat = pd.concat(nats_df)
if profile_option == 'jobs':
    a = px.bar(total_jobs,x=profile_option,y='Percent',barmode='group',
    orientation='v',
    color='Brand')
    a.update_layout(xaxis={'categoryorder': 'total ascending'})

    st.plotly_chart(a, use_container_width=True)
elif profile_option =='interests':
    a = px.bar(total_ints,x=profile_option,y='Percent',barmode='group',
    orientation='v',
    color='Brand')
    a.update_layout(xaxis={'categoryorder': 'total ascending'})

    st.plotly_chart(a, use_container_width=True)
elif profile_option =='nationality':
    a = px.bar(total_nat,x=profile_option,y='Percent',barmode='group',
    orientation='v',
    color='Brand')
    a.update_layout(xaxis={'categoryorder': 'total ascending'})

    st.plotly_chart(a, use_container_width=True)
else:
    a = px.bar(total_city,x=profile_option,y='Percent',barmode='group',
    orientation='v',
    color='Brand')
    a.update_layout(yaxis={'categoryorder': 'total ascending'})

    st.plotly_chart(a, use_container_width=True)
