import streamlit as st
from style import local_css

st.set_page_config(
    page_title="Developer Salary Predictor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Inject custom CSS for a modern look
local_css()

from predict_page import show_predict_page
from explore_page import show_explore_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()