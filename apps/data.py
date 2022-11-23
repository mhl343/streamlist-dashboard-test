import streamlit as st
def app():
    st.header('Display Athlete')
    option = st.selectbox(
    'Select Athlete',
    ('Athlete 1', 'Athlete 2', 'Athlete 3'))
    st.write('Stats about ', option, ':')