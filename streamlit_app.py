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
st.dataframe(my_fruit_list)
