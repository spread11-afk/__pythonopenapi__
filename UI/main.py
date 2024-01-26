import requests
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh


st_autorefresh(interval=10000,limit=100,key='fizzbuzzcounter')

url = 'https://openapi-test-miif.onrender.com/pico_w/?count=5'

r = requests.get(url=url)

if r.status_code == 200:
    data = r.json()
    print('success')

df = pd.DataFrame(data)

st.title("阿阿阿阿阿:sunglasses:")
st.header("呵呵呵呵呵")
st.write(df)
st.caption('dsfskldnfl : blue[colors] and emojis :sungalsses:')
st.caption('afasdjpoaf:sunglasses:')
st.caption("光線")
st.line_chart(df,x='date',y='light')
st.line_chart(df,x='date',y='temperature',color='#ff0000')