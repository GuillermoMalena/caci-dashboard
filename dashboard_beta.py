
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
import os

### Get folder paths for subdirectories
brand_profiles = ('./brand_profiles')
brand_avgs = ('./brand_means')

##set header

st.set_page_config(page_title='Caci Twitter Analyzer',  layout='wide', page_icon=':chart_with_upwards_trend:')


## Import Brands Key
brands_csv = pd.read_csv('brands_key.csv')
brands_list = brands_csv['User']
#selected_brand = brands_csv.loc[brands_csv['User'] == option]
#profile_pic = selected_brand['Profile Picture URL'].reset_index(drop=True)[0]


a1,a2 = st.columns([2,1])
with a1:
     st.title("Welcome to Caci Twitter Analyzer")
     option = st.selectbox(
     'Which Twitter handle do you want to analyze?',
      brands_list)
     selected_brand = brands_csv.loc[brands_csv['User'] == option]
     profile_pic = selected_brand['Profile Picture URL'].reset_index(drop=True)[0]
with a2:
     def load_lottieurl(url: str):
          r = requests.get(url)
          if r.status_code != 200:
               return None
          return r.json()


     lottie = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_0eaqa2gh.json')
     st_lottie(lottie, speed=1, height=250,width=400, key="initial")

## Pull in categories and entities
#brands_csv = pd.read_csv('brands_key.csv')
#selected_brand = brands_csv.loc[brands_csv['User'] == option]
category1 = selected_brand['Category Level 1'].reset_index(drop=True)[0]
category2 = selected_brand['Category Level 2'].reset_index(drop=True)[0]

#Pull the profile databases
option = option.lower()
filename = f'{option}_jobs.csv'
jobs = pd.read_csv(os.path.join(brand_profiles,f'{option}_jobs.csv'),dtype=str).head(15)
nat = pd.read_csv(os.path.join(brand_profiles,f'{option}_nationality.csv'),dtype=str).head(15)
ints = pd.read_csv(os.path.join(brand_profiles,f'{option}_interests.csv'),dtype=str).head(15)
cities = pd.read_csv(os.path.join(brand_profiles,f'{option}_city.csv'),dtype=str).head(15)
fam = pd.read_csv(os.path.join(brand_profiles,f'{option}_family.csv'),dtype=str)

# Rename columns
nat = nat.rename(columns ={f'{option}_percent':'Percent'})
nat['Percent'] = nat['Percent'].astype(float).round(2)
nat['Brand'] = option

jobs = jobs.rename(columns ={f'{option}_percent':'Percent'})
jobs['Percent'] = jobs['Percent'].astype(float).round(2)
jobs['Brand'] = option

cities = cities.rename(columns ={f'{option}_percent':'Percent'})
cities['Percent'] = cities['Percent'].astype(float).round(2)
ints = ints.rename(columns ={f'{option}_percent':'Percent'})
ints['Percent'] = ints['Percent'].astype(float).round(2)
ints['Brand'] = option

fam = fam.rename(columns ={f'{option}_percent':'Percent'})
fam['Percent'] = fam['Percent'].astype(float).round(2)



## get top values
top_nat = round(float(nat.iloc[0,:]['Percent']),2)
top_nat_str = nat.iloc[0,:]['nationality']

top_jobs = round(float(jobs.iloc[0,:]['Percent']),2)
top_job_str = jobs.iloc[0,:]['jobs']

cities = cities.rename(columns ={f'{option}_percent':'Percent'})
top_cities = round(float(cities.iloc[0,:]['Percent']),2)
top_city_str = cities.iloc[0,:]['city']


## get equivalent averages
avg_jobs = pd.read_csv(os.path.join(brand_avgs,f'Music_Rapper_job_avg.csv'),dtype=str)
avg_jobs = avg_jobs.rename(columns={'job':'jobs','w_avg':'Percent'}).head(15)
avg_jobs = avg_jobs[['jobs','Percent']]
avg_jobs['Percent'] = avg_jobs['Percent'].astype(float).round(2)
avg_jobs['Brand'] = 'Average'
avg_jobs_top = avg_jobs.loc[avg_jobs['jobs'] == jobs.iloc[0,:]['jobs']]
avg_jobs_val =  round(float(avg_jobs_top.iloc[0,:]['Percent']),2)

avg_nat = pd.read_csv(os.path.join(brand_avgs,f'Music_Rapper_nationality_avg.csv'),dtype=str)
avg_nat = avg_nat.rename(columns={'job':'jobs','w_avg':'Percent'})
avg_nat = avg_nat[['nationality','Percent']]
avg_nat['Percent'] = avg_nat['Percent'].astype(float).round(2)
avg_nat['Brand'] = 'Average'
avg_nat_top = avg_nat.loc[avg_nat['nationality'] == nat.iloc[0,:]['nationality']]
avg_nat_val =  round(float(avg_nat_top.iloc[0,:]['Percent']),2)

avg_city = pd.read_csv(os.path.join(brand_avgs,f'Music_Rapper_city_avg.csv'),dtype=str)
avg_city = avg_city[['city','w_avg','Category Level 1','Category Level 2','Entity']]
avg_city = avg_city.loc[avg_city['city'] == cities.iloc[0,:]['city']]
avg_city_val = round(float(avg_city.iloc[0,:]['w_avg']),2)

avg_ints = pd.read_csv(os.path.join(brand_avgs,f'Music_Rapper_interests_avg.csv'),dtype=str)
avg_ints = avg_ints.rename(columns={'w_avg':'Percent'}).head(15)
avg_ints = avg_ints[['interests','Percent']]
avg_ints['Percent'] = avg_ints['Percent'].astype(float).round(2)
avg_ints['Brand'] = 'Average'

## get diffs
job_diff = round(top_jobs - avg_jobs_val,2)
nat_diff = round(top_nat - avg_nat_val,2)
city_diff = round(top_cities - avg_city_val,2)

m1,m2,m3 = st.columns((1,1,1))
m1.metric(label='Top Audience Nationality', value=f'{top_nat_str} ({top_nat}%)',
          delta=str(nat_diff) + f'% Compared to average {category2} category')
m2.metric(label='Top Audience Job/Profession', value=f'{top_job_str} ({top_jobs}%)',
          delta=str(job_diff) + f'% Compared to average {category2} category')
m3.metric(label='Top Audience City', value=f'{top_city_str}  ({top_cities}%)',
          delta=str(city_diff) +  f'% Compared to average {category2} category')

col1, col2 = st.columns(2)
with col1:
     total_jobs = jobs.append(avg_jobs)
     total_jobs = total_jobs[total_jobs.duplicated(subset=['jobs'], keep=False)]
     st.subheader("Top follower jobs")
     #st.dataframe(total_jobs)
     a = px.bar(total_jobs,x='Percent',y="jobs",barmode='group',orientation='h',color='Brand')
     a.update_layout(yaxis={'categoryorder': 'total ascending'})

     st.plotly_chart(a, use_container_width=True)

with col2:
     total_ints = ints.append(avg_ints)
     st.subheader("Top follower interests")
     total_ints = total_ints[total_ints.duplicated(subset=['interests'], keep=False)]

     b = px.bar(total_ints, x='Percent', y="interests", barmode='group', orientation='h', color='Brand')
     b.update_layout(yaxis={'categoryorder': 'total ascending'})
     st.plotly_chart(b, use_container_width=True)
     # st.subheader("Top follower interests")
     # b = px.bar(ints, x='Percent', y="interests")
     # st.plotly_chart(b, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
     st.subheader("Top follower nationalities")
     total_nat = nat.append(avg_nat)
     total_nat = total_nat[total_nat.duplicated(subset=['nationality'], keep=False)]
     # c = px.bar(total_nat, y="Percent",x='nationality', barmode='group', color='Brand',orientation='v')
     # c.update_layout(yaxis={'categoryorder': 'total ascending'})
     # st.plotly_chart(c, use_container_width=False)

     fig = px.pie(nat, values=f'{option}_count', names='nationality', title='Most frequent nationalities among brand followers')
     st.plotly_chart(fig, use_container_width=True)



## Map
with col4:
     st.subheader("Top follower cities")

     city_geo = pd.read_csv('city_coordinates.csv')[['city','lat','lon']]
     city_map = cities.merge(city_geo,how='inner',left_on='city',right_on='city')[['city','Percent','lat','lon']]
     city_map['Percent'] = city_map['Percent'].astype(float)
     map_fig = px.scatter_geo(city_map, lat = 'lat',lon='lon', color="city",
                          hover_name="city", size="Percent",scope='usa')
     st.plotly_chart(map_fig, use_container_width=True)

# st.subheader(f"Top brand recommendations based on those who follow {option}")
#
#
# z = pd.read_csv(f'{option}_recommendations.csv').head(15)
#
# d= px.bar(z, y='Normalized', x="User",orientation='v')
# d.update_layout(xaxis={'categoryorder': 'total descending'})
# st.plotly_chart(d, use_container_width=True)




