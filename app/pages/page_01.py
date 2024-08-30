import streamlit as st

st.header('Welcome to Streamlit!')

import base64

@st.cache_data
def load_image(path):
    with open(path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return encoded

def image_tag(path):
    encoded = load_image(path)
    tag = f'<img src="data:image/png;base64,{encoded}">'
    return tag

def background_image_style(path):
    encoded = load_image(path)
    style = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
    }}
    </style>
    '''
    return style

image_path = 'images/python.png'
image_link = 'https://docs.python.org/3/'


st.write(f'<a href="{image_link}">{image_tag(image_path)}</a>', unsafe_allow_html=True)

if st.checkbox('Show background image', False):
    st.write(background_image_style(image_path), unsafe_allow_html=True)

if st.button('More 🎈🎈🎈 please!'):
    st.balloons()
