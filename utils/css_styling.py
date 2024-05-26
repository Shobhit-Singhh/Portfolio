import streamlit as st

def technical_skill_custom_style():
    """Sets custom CSS styles for the Streamlit app."""
    st.markdown("""
    <style>
    .reportview-container {
        background: #f5f5f5;
    }
    .stHeader {
        font-size: 2.5em;
        text-align: center;
        color: #4B4B4B;
        font-weight: bold;
    }
    .stMarkdown {
        margin: 50px 10;
        text-align: center;
    }
    .skill-entry {
        min-height: 10px;  
        display: flex;
        flex-direction: column;
        justify-content: center;
        text-align: left;
        padding: 10px;
    }
    .skill-name {
        font-size: larger;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .skill-percentage {
        text-align: left;
        padding-top: 0 px;
    }
    .skill-message {
        font-size: small;
        font-style: italic;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

def certificate_custom_css():
    st.markdown("""
    <style>
    .reportview-container {
        background: #f5f5f5;
    }
    .stHeader {
        font-size: 2.5em;
        text-align: center;
        color: #4B4B4B;
        font-weight: bold;
    }
    .stMarkdown {
        margin: -50px 10;
        text-align: center;
    }
    .certificate-entry {
        min-height: 200px; /* Adjust the height as needed */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 10px;
    }
    .certificate-entry .title {
        font-size: 1.5em;
        margin-bottom: 10px;
    }
    .certificate-entry .issuer, .certificate-entry .link {
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)
