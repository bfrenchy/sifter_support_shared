"""
This module goes through the basics of the streamlit library
"""

# In the terminal, typing `streamlit hello` will open a page in the browser.
# `streamlit run streamlit_demo.py`` will open our app in the browser
# control-C will quit the app

import streamlit as st
import pandas as pd

st.title("Our first Streamlit example :fire:")

# Displaying data on the screen:
# 1. st.write()
# 2. Magic

# st.write("We learnin Streamlit...")  in terminal `streamlit run streamlit_demo.py`
l1 = [0,1,2]
st.write(l1)

l2 = list('abc')
d1 = dict(zip(l1, l2))
st.write(d1)

# using Magic
# enterint the text is automatically written to the web app.
'Displaying using Magic :smile:'
"That's crazy"

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20,30, 40]
})

df  # equivalent to `st.write(df)`


