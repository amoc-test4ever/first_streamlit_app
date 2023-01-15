import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

st.title ("My MOM's new healthy Dinner")
st.header('🥣 🥗 🐔 🥑🍞 Breakfast Menu 🥣 🥗 🐔 🥑🍞')
st.text('🥗 Curry Omega 3 & Blueberry Oatmeal')
st.text('🥑🍞 Sandwich Kale, Spinach & Rocket Smoothie')
st.text('🐔 Cooking Hard-Boiled Free-Range Egg')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = st.multiselect("Pick Some Fruits", list(my_fruit_list.index),['Avocado','Strawberries'])

fruit_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruit_to_show)

# create a repeated code boack
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)            
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  # new  section to display fruityvice api  response
st.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = st.text_input('What fruit would you like information about?')
    if not fruit_choice:
        st.error('Please select a fruit to get information.')
    else:
        back_from_function=get_fruityvice_data(fruit_choice)
        st.dataframe(back_from_function)
                                 
except URLError as e:
    st.error()                            
#st.stop();
st.header("The Fruit Load List Contains:")
#Snowflake related function

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()

#Add button to load the fruit
if st.button('Get Fruit Load List:'):
   my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
   my_data_rows= get_fruit_load_list()
   st.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values ('" + jackfruit + "')")
      return "Thanks for adding" +new_fruit
      #return my_cur_fetchall()


add_my_fruit = st.text_input('What fruit would you like to add?','jackfruit')
st.write('The user entered ', add_my_fruit)
