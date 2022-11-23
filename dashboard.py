import streamlit as st
from multiapp import MultiApp
from apps import home, data, model

app = MultiApp()
st.title('Baseball College Athlete Dashboard')
app.add_app("Homepage", home.app)
app.add_app("Display", data.app)
app.add_app("Predict", model.app)

app.run()
