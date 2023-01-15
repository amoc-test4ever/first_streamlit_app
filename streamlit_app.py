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

st.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "apple")
# st.text(fruityvice_response)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)
