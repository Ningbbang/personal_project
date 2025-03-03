import streamlit as st
import pandas as pd
from datetime import datetime


st.set_page_config('WTM','','wide')
df = pd.read_excel('data.xlsx')
df['날짜'] = pd.to_datetime(df['날짜']).dt.date

with st.sidebar:
    st.write('근무시간 조회')
    st.selectbox('사번 :', ['22404099'])
    st.write('성명 : 이장은')
    target_date = st.slider('날짜 검색', 1, 12)

st.write(str(target_date)+'월 근무시간')
st.write('총 근무시간 : ',229,":",0)
st.write('휴일 근무시간 : ',29,":",40)

st.dataframe(df)