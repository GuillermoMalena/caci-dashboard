import streamlit as st
from annotated_text import annotated_text
import pandas as pd
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
import os

brand_db = r'/Users/GuillermoMalena_1/Desktop/Cacicazgo/Code/twitter_scraper/brand_db/'

brand_profiles = ('./brand_profiles')
brand_avgs = ('./brand_means')
    
brands_key_df = pd.read_csv(r'/Users/GuillermoMalena_1/Desktop/Cacicazgo/Code/twitter_scraper/brands_key.csv',dtype={'User ID':'string'})
brands_key_list = brands_key_df['User'].to_list()

brands_cat_list = []
for i in brands_key_list:
    brands_key_filepath = os.path.join(brand_db,f'{i.lower()}_followers.csv')
  
    if os.path.isfile(brands_key_filepath) is True:
     
        i = i.lower()
        brands_cat_list.append(i)
brands_list = brands_cat_list


brands = st.multiselect(
    "Choose brands", brands_list, ["kendricklamar", "drake"]
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
profile_option = st.radio("Choose a profile to analyze the brands for",profiles,1 )

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
# else:
#     st.subheader("Top follower interests")
        

#     b = px.bar(ints, x='Percent', y="interests", barmode='group', orientation='h', color='Brand')
#     b.update_layout(yaxis={'categoryorder': 'total ascending'})
#     st.plotly_chart(b, use_container_width=True)
# col1, col2 = st.columns(2)
# if len(brands) < 2:
#     st.subheader("Top follower jobs")
      
#     a = px.bar(jobs,x='Percent',y="jobs",barmode='group',orientation='h',color='Brand')
#     a.update_layout(yaxis={'categoryorder': 'total ascending'})

#     st.plotly_chart(a, use_container_width=True)

# elif 
#     with col1:
       
#         st.subheader("Top follower jobs")
      
#         a = px.bar(jobs,x='Percent',y="jobs",barmode='group',orientation='h',color='Brand')
#         a.update_layout(yaxis={'categoryorder': 'total ascending'})

#         st.plotly_chart(a, use_container_width=True)

#     with col2:
#         # total_ints = ints.append(ints_1)
#         st.subheader("Top follower interests")
        

#         b = px.bar(ints, x='Percent', y="interests", barmode='group', orientation='h', color='Brand')
#         b.update_layout(yaxis={'categoryorder': 'total ascending'})
#         st.plotly_chart(b, use_container_width=True)
      
# else:

#     with col1:
#         total_jobs = pd.concat(jobs_df)
#         total_jobs = total_jobs[total_jobs.duplicated(subset=['jobs'], keep=False)]
#         st.subheader("Top follower jobs")
#         #st.dataframe(total_jobs)
#         a = px.bar(total_jobs,x='Percent',y="jobs",barmode='group',orientation='h',color='Brand')
#         a.update_layout(yaxis={'categoryorder': 'total ascending'})

#         st.plotly_chart(a, use_container_width=True)

#     with col2:
#         total_ints = pd.concat(ints_df)
#         st.subheader("Top follower interests")
#         total_ints = total_ints[total_ints.duplicated(subset=['interests'], keep=False)]

#         b = px.bar(total_ints, x='Percent', y="interests", barmode='group', orientation='V', color='Brand')
#         b.update_layout(yaxis={'categoryorder': 'total ascending'})
#         st.plotly_chart(b, use_container_width=True)
#         # st.subheader("Top follower interests")
#         # b = px.bar(ints, x='Percent', y="interests")
#         # st.plotly_chart(b, use_container_width=True)