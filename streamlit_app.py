import streamlit as st
st.title('My Parents New Healthy Diner')
   
st.header('Breakfast Menu')
st.text('🥣 Omega 3 and Blueberry oat Meal')
st.text('🥗 kale spianch and Rocket Smoothis')
st.text('🐔 Hard-boled free range Egg')
st.text('🥑🍞 Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected= st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
st.dataframe(fruits_to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
