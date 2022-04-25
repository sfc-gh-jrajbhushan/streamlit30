import streamlit as st 
import datetime

today = datetime.datetime.now()
future = datetime.datetime(2023,2,20,12,00,00,00000)
diff = future - today


st.header('Fully Vested : Feb 20 2023 12:00 AM :sunglasses:')
print(diff)
st.subheader(diff)

st.markdown("![Alt Text](https://media.giphy.com/media/l1J9CuIY0jSj1q0la/giphy.gif)")



