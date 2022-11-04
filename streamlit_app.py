import streamlit
import pandas

streamlit.title('Testing out Streamlit')
streamlit.header('A Headline')
streamlit.text('Lorem Ipsum dolor sit amet.')

fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_list = fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('Pick some fruit',list(fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
