import streamlit as st
from covid19 import Covid19Data
from draw_graph_matplotlib import DrawGraphMatplotlib
from latest_info import LatestInfo

PREFECTURE = {
        '全国': ['ALL', 'Japan'],
        '東京': ['Tokyo', 'Tokyo'],
        '神奈川': ['Kanagawa', 'Kanagawa']
    }

graph_kind = st.sidebar.selectbox(
    'ライブラリを選択',
    ['Matplotlib', 'Plotly']
)

st.title('Covid-19 graph by Streamlit')

prefecture_selectbox = st.selectbox(
    '県を選択してください。',
    ('全国', '東京', '神奈川'))

c19d = Covid19Data()
l_info = LatestInfo()

latest_info_message = l_info.get_latest_info(
    c19d.all_data_df[['Date', PREFECTURE[prefecture_selectbox][0]]],
    PREFECTURE[prefecture_selectbox][0],
    prefecture_selectbox)

st.subheader('＜最新情報＞', anchor=None)
st.write(latest_info_message)

st.subheader(f'＜{prefecture_selectbox}の陽性者数の推移＞', anchor=None)
if graph_kind == 'Matplotlib':
    dgm = DrawGraphMatplotlib()
    fig = dgm.draw_bar_graph(
        c19d.all_data_df[['Date', PREFECTURE[prefecture_selectbox][0]]],
        PREFECTURE[prefecture_selectbox][0],
        PREFECTURE[prefecture_selectbox][1])
    st.pyplot(fig)
    
elif graph_kind == 'Plotly':
    st.write('工事中')

# streamlit hello
# streamlit run app.py
