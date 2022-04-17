import streamlit as st 

st.header('st.button')

if st.button('Say Hello', help='stop hovering over me'):
	st.write('why hello there')
else:
	st.write('goodbye')


#--- 
# st.write
# st.header
# st.button(Button1):  st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, disabled=False)
# st.write writes under wherever it is 