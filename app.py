import streamlit as st
import pandas as pd
import numpy as np

st.title('Sample App')

if st.button('Click me!'):
    st.write('Clicked!')
    
if st.checkbox('Please check!'):
    st.write('Checked!')
    
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write('You selected:', options)

left_col, right_col = st.columns(2)

left_number = left_col.slider('Pick a Num', 0, 100, 50)
right_col.write(f'Number: {left_number}')

number = st.sidebar.slider('Pick a Num', 0, 100, 40)
st.sidebar.write(f'Number: {number}')

# streamlit hello
# streamlit run app.py
