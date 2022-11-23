import streamlit as st
def app():
    name = st.text_input('Enter Athlete Name', '')
    if name == "Maddie":
        st.markdown('Predicted companies: A, B, C')
    st.markdown("""---""")
    features = st.subheader('Filter by Athlete Characteristics')
    values = st.slider(
    'Amount of Instagram Followers',
    0.0, 10.0, (0.0, 10.0))
    st.write('Values:', values)