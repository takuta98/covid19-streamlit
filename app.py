import streamlit as st
from draw_graph_matplotlib import *

graph_kind = st.sidebar.selectbox(
    'ライブラリを選択',
    ['Matplotlib', 'Plotly']
)

st.title('Covid-19 graph by Streamlit')

prefecture_selectbox = st.selectbox(
    '県を選択してください。',
    ('全国', '東京', '神奈川'))

if graph_kind == 'Matplotlib':
    dgm = DrawGraphMatplotlib()
    fig = dgm.draw_bar_graph(prefecture_selectbox)
    st.pyplot(fig)
    
elif graph_kind == 'Plotly':
    st.write('工事中')

# streamlit hello
# streamlit run app.py
