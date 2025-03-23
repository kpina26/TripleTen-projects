import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st


st.header('Car Advertisement')

df_cars = pd.read_csv('./vehicles_us.csv')
df_cars[['make', 'model']]= df_cars['model'].str.split(' ', n=1, expand=True)
df_cars['date_posted'] = pd.to_datetime(df_cars['date_posted'], format='%Y-%m-%d')

df_cars['odometer'].fillna(df_cars.groupby(['model_year', 'model'])['odometer'].transform('median'), inplace=True)
df_cars['odometer'] = np.ceil(df_cars['odometer'].fillna(df_cars['odometer'].median()))

print(np.array_equal(df_cars['odometer'], df_cars['odometer'].astype('int')))
if np.array_equal(df_cars['odometer'], df_cars['odometer'].astype('int')):
    df_cars['odometer'] = df_cars['odometer'].astype('int')

df_cars['cylinders'] = df_cars['cylinders'].fillna(0).astype('int64')
df_cars['model_year'] = df_cars['model_year'].fillna(df_cars['model_year'].median()).astype('int64')

df_cars['is_4wd']= df_cars['is_4wd'].fillna(0).astype(bool)

df_cars['paint_color'] = df_cars['paint_color'].fillna('unknown')


fig= px.scatter(df_cars, y="price", x="make", color="paint_color")
fig.update_traces(marker_size=15)
fig.update_layout(scattermode="group", title_text='Price by Paint Color', xaxis_title='Vehicle Make', yaxis_title='Vehicle Price')
st.plotly_chart(fig)
st.write('This graph shows the distribution of vehicle prices across different manufacturers, showing significant price variability among brands, the prevalence of common paint colors like white and black, the presence of outliers such as high-priced Nissan vehicles, and potential data gaps with the "unknown" category, highlighting trends in market pricing and consumer preferences.')

toggle_make = st.checkbox("Show by Make instead of Model")
x_axis_column = "make" if toggle_make else "model"
st.subheader(f"Vehicle Prices by {'Make' if toggle_make else 'Model'}")

fig = px.histogram(df_cars, x=x_axis_column, color="condition")
fig.update_layout(title_text='Coniditions of Vehicles', xaxis_title='Model Year', yaxis_title='Quantities')
st.plotly_chart(fig)
st.write('This histogram shows the distribution of vehicle model years and their conditions, indicating that most vehicles in the dataset are from the 2000s and later, with a significant peak around a particular recent year. The majority of vehicles are categorized as being in "good" condition, followed by "like new" and "fair" conditions, while fewer vehicles are marked as "excellent," "salvage," or "new." The trend suggests that older vehicles are less frequent, likely due to attrition over time, while newer vehicles dominate the dataset, reflecting market availability and consumer demand.')




