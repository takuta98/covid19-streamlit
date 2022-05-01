import streamlit as st
from covid19 import *
import matplotlib.pyplot as plt

st.title('Covid-19 graph by Streamlit')

prefecture_selectbox = st.selectbox(
    '県を選択してください。',
    ('全国', '東京', '神奈川'))

prefecture = {
    '全国': ['ALL', 'Japan'],
    '東京': ['Tokyo', 'Tokyo'],
    '神奈川': ['Kanagawa', 'Kanagawa']
}
        
c19d = Covid19Data()
data_df = c19d.get_new_cases_covid19(prefecture[prefecture_selectbox][0])
date_df = c19d.get_date()


fig = plt.figure(
    figsize=(10, 5),
    dpi=150,
    facecolor='orange',
    edgecolor='black',
    linewidth=5,
    tight_layout=True)

ax = fig.add_subplot(
    111, 
    facecolor='black',
    xlabel='Date',
    ylabel='PCR positive daily in '+prefecture[prefecture_selectbox][1])

ax.bar(
    date_df, 
    data_df,
    color='white')

st.write
st.pyplot(fig)



# streamlit hello
# streamlit run app.py
