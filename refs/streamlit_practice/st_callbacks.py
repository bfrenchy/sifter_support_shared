# CALLBACKS

import streamlit as st
st.subheader('Distance converter')

def miles_to_km():
    st.session_state.km = st.session_state.miles * 1.609

def km_to_miles():
    st.session_state.miles = st.session_state.km * 0.621

col1, buff, col2 = st.columns([2, 1, 2])  # buffer column is half as big as col1 or col2
with col1:
    miles = st.number_input("Miles:", key="miles", on_change=miles_to_km)  # on_change is the callback

with col2:
    km = st.number_input("KM:", key="km", on_change=km_to_miles)

# When streamlit detects a change in either the miles or km input,
# it reruns the script to update the other widget.