import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('Testing out Streamlit')
streamlit.header('A Headline')
streamlit.text('Lorem Ipsum dolor sit amet.')

fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_list = fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect('Pick some fruit',list(fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:
        fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute('SELECT * FROM fruit_load_list')
my_data_rows = my_cur.fetchall()
streamlit.text('Hello from Snowflake')
streamlit.dataframe(my_data_rows)

streamlit.text('Add new fruit')
new_fruit = streamlit.text_input('What fruit do you want to add', 'jackfruit')
