import streamlit as st
import numpy as np
import pandas as pd

#st.write("Hello World")
#age=st.text_input("What is your name")
#st.write(f"You are {age} years old")
#if st.button('click me'):
#    st.write_stream('Hello World!')

chart_data=pd.DataFrame(np.random.randn(20,3), columns=["a","b","c"])
st.write(chart_data)

 
#data = pd.read_csv("movies.csv")
#st.write(data)