import streamlit as st

def local_css():
    """Injects custom CSS into the Streamlit app to provide a modern look and feel."""
    css = """
    <style>
    /* Hide default Streamlit header and footer */
    header, footer {visibility: hidden;}

    /* Overall page background */
    body, .stApp {
        background: linear-gradient(135deg, #1f1c2c 0%, #928dab 100%);
        color: #FFFFFF;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] > div:first-child {
        background: #2c2a4a;
        padding-top: 2rem;
    }
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {
        color: #ffffff;
    }

    /* Selectbox & Input widgets */
    div[data-baseweb="select"] > div {
        background-color: #3d3b5b;
        border-radius: 8px;
        border: none;
        color: #ffffff;
    }

    /* Buttons */
    .stButton > button {
        color: #fff;
        background-color: #6c63ff;
        border-radius: 8px;
        padding: .5rem 1.25rem;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #9795f0;
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0,0,0,.2);
    }

    /* Slider colors */
    .stSlider > div:nth-child(1) > div {
        color: #6c63ff;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)