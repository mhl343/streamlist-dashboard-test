import streamlit as st
import pandas as pd
from multiapp import MultiApp
from apps import display, home, predict

app = MultiApp()
st.title('Baseball College Athlete Dashboard')
app.add_app("Homepage", home.app)
app.add_app("Display", display.app)
app.add_app("Predict", predict.app)

app.run()
