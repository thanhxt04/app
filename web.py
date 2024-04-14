import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title ("Interactive Dashboard")
st.header("Interact with this dashboard using the widgets on the sidebar")

st.sidebar.title("This is written inside the sidebar") 

#lấy dữ liệu
movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/movies.csv")
#Tóm tắt
movies_data.info()
#Loại bỏ cột dữ liệu thiếu
movies_data.dropna()


# Sidebar for filtering
st.sidebar.header('Filter Options')


# Lọc theo thể loại 
selected_genres = st.sidebar.multiselect('Select Genre', ['Animation','Horror','Fantasy','Romance'] + sorted(movies_data['genre'].unique()), default=['Animation','Horror','Fantasy','Romance'])
# Lọc theo năm
selected_year = st.sidebar.selectbox('Select Year', sorted(movies_data['year'].unique()))
# Apply filters
if 'All' in selected_genres:
    filtered_movies = movies_data[movies_data['year'] == selected_year]
else:
    filtered_movies = movies_data[(movies_data['year'] == selected_year) & 
                             (movies_data['genre'].isin(selected_genres))]



#in ra danh sách
st.write('Filtered Movies:')
#đánh số thứ tự list
filtered_movies_reset_index = filtered_movies.reset_index(drop=True)
st.table(filtered_movies[['name','genre','year']])

#Biểu đồ dưới 
st.write("""Average Movie Budget, Grouped by Genre""")
avg_budget = movies_data.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

fig = plt.figure(figsize = (19, 10))
plt.bar(genre, avg_bud, color = 'maroon')
plt.xlabel('genre')
plt.ylabel('budget')
plt.title('Matplotlib Bar Chart Showing the Average \
Budget of Movies in Each Genre')

st.pyplot(fig)


