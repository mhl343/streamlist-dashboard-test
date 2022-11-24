import streamlit as st
def app():
    name = st.text_input('Enter Athlete Name', '')
    if name == "Maddie":
        st.markdown('Predicted companies: A, B, C, D')
    st.markdown("""---""")
    features = st.subheader('Filter by Athlete Characteristics')
    
    school = st.text_input('Enter School Name', '')
    
    instagram = st.slider(
    'Amount of Instagram Followers',
    0.0, 10.0, (0.0, 10.0))
    st.write('Values:', instagram)

    twitter = st.slider(
    'Amount of Twitter Followers',
    0.0, 10.0, (0.0, 10.0))
    st.write('Values:', twitter)

    tiktok = st.slider(
    'Amount of TikTok Followers',
    0.0, 10.0, (0.0, 10.0))
    st.write('Values:', tiktok)
