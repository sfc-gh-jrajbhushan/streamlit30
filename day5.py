import streamlit as st 
# st.write(), st.markdown()
# display python dict
# display pandas DF as table
# plot: matplotlib, plotly, altair, graphviz, bokeh 

import numpy as np 
import altair as alt 
import pandas as pd 

st.header('st.write')
st.write('Hello, *World!*, :sunglasses:')
# regular: Hello           italic: *World!*       emoji :sunglasses:
st.write(1234)
st.header('Header test')
st.subheader('SH test')
st.caption('caption test')
st.text('text test')
st.latex('latex test')
st.code('select * from table',language="python")

df = pd.DataFrame({
	'first column':[1,2,3,4],
	'second column': [10,20,30,40]
	})

st.write(df)
st.write('below is df', df, 'above is df')

df2 = pd.DataFrame(
	np.random.randn(200,3),
	columns=['a','b','c'])
c = alt.Chart(df2).mark_circle().encode(x='a',y='b',color='c', tooltip=['a','b','c'])
st.write(c)
st.write(df2)

