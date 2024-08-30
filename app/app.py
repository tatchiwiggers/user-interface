import streamlit as st
import requests
import numpy as np


st.set_page_config(page_title='Hello', page_icon= ';')

st.markdown('# Streamlit is awesome!')

if st.button('click ;)'):
    st.image('images/LW.png')


query = st.text_input('Search a GIF')
url = 'https://api.giphy.com/v1/gifs/search'
params = {'api_key': st.secrets.api_key, 'q': query, 'limit':10}
response = requests.get(url=url, params=params).json()

while not query:
    st.stop()


gif_url = response['data'][np.random.randint(0, 10)]['embed_url']

st.write(
    f'<iframe src="{gif_url}" width="480" height="240">',
    unsafe_allow_html=True,
)

# st.write(st.secrets['a_new_section']['magic'])

# st.write( st.secrets.some_key)
