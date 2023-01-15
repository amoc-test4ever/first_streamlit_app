


import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


st.title('My Parents New Healthy Diner')
   
st.header('Breakfast Menu')
st.text('🥣 Omega 3 and Blueberry oat Meal')
st.text('🥗 kale spianch and Rocket Smoothis')
st.text('🐔 Hard-boled free range Egg')
st.text('🥑🍞 Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected= st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# Display the table on the page.
st.dataframe(fruits_to_show)


def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice )
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized


st.header("Fruityvice Fruit Advice!")
   
try:
   fruit_choice = st.text_input('What fruit would you like information about?')
   if not fruit_choice:
      st.error("Please select  a fruit to get information")
   else:
         #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice )
         #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
         #st.dataframe(fruityvice_normalized)
         back_from_function= get_fruityvice_data(fruit_choice)
         st.dataframe(back_from_function)
except URLError as e:
    st.error()
   
#st.write('The user entered ', fruit_choice)
# st.text(fruityvice_response)
# write your own comment -what does the next line do? 
# write your own comment - what does this do?




st.stop()

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
my_cur.execute("insert into fruit_load_list values ('from st')")
my_data_rows = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)


add_my_fruit = st.text_input('What fruit would you like to add?','jackfruit')
st.write('The user entered ', add_my_fruit)


