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


def education_custom_style():
    """Sets custom CSS styles for the Streamlit education page."""
    st.markdown("""
    <style>
    .reportview-container {
        background: #f5f5f5;
        padding: 20px;
    }
    .stHeader {
        font-size: 2.5em;
        text-align: center;
        color: #4B4B4B;
        font-weight: bold;
        margin-bottom: -20px;
    }
    .stMarkdown {
        margin: 0px 10px;
        text-align: center;
    }
    .education-entry {
        background: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        padding: 2px;
        margin-bottom: 20px;
    }
    .degree-name {
        font-size: 3em;
        font-weight: bold;
        color: #333;
        margin-bottom: 5px;
    }
    .college-name {
        font-size: 2em;
        color: #777;
        margin-bottom: 10 px;
        display: flex;
        justify-content: space-between;
    }
    .course-details {
        font-size: 1em;
        color: #555;
        line-height: 1.6em;
        text-align: left;
    }
    .course-details ul {
        padding-left: 20px;
        margin-top: 10px;
    }
    .course-details ul li {
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)


def project_custom_style():
    """Sets custom CSS styles for the Project Details section in Streamlit."""
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
        margin: 5px 10px;
        text-align: left;
    }
    .project-box {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .project-box-header {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .project-box-content {
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    """Sets custom CSS styles for the Project Details section in Streamlit."""
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
        text-align: left;
    }
    
    .project-title {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .project-description {
        font-size: 16px;
        color: #666;
        margin-bottom: 10px;
    }
    .project-message {
        font-size: 14px;
        font-style: italic;
        color: #888;
    }
    .project-section {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        margin-bottom: 20px;
        background-color: #f9f9f9;
    }
    
    .project-box-content {
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)