import streamlit
import pandas

streamlit.title('Testing out Streamlit')
streamlit.header('A Headline')
streamlit.text('Lorem Ipsum dolor sit amet.')

fruit_list = pandas.read('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(fruit_list)
