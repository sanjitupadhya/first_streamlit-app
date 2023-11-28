import streamlit  

streamlit.title('Hello')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
               
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

#option of fruit by name
my_fruit_list = my_fruit_list.set_index('Fruit')

# using multi select o pick the desired fruits for the smoothie
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index,['Avocado','Strawberries']))
streamlit.dataframe(my_fruit_list)
