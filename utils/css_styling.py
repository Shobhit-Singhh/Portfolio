import streamlit as st


def technical_skill_custom_style():
    """Sets custom CSS styles for the Technical Skills section in Streamlit."""
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
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .skill-entry h1 {
        font-size: 1px;
        color: #333;

    }
    
    .skill-entry h2 {
        font-size: 30px;
        color: #444;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;  /* Adjust margin as needed */
    }
    
    .skill-entry .skill-name {
        font-size: 30px;
        font-weight: bold;
        color: #444;
        
    }
    
    .skill-entry .skill-percentage {
        text-align: left;
        padding-top: 5px;  /* Adjust padding as needed */
    }
    
    .skill-entry .skill-message {
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
    """Sets custom CSS styles for the Education Details section in Streamlit."""
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
    .degree-entry {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .degree-entry h2 {
        font-size: 30px;
        color: #444;
        text-align: center;
        font-weight: bold;
    }
    .degree-entry h3 {
        font-size: 20px;
        color: #444;
        margin-bottom: 8px;
    }
    .degree-entry p {
        font-size: 16px;
        color: #555;
        line-height: 1.6em;
        text-align: left;
    }
    .custom-separator {
        border: none;
        border-top: 2px solid #ddd;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)


def experience_custom_style():
    """Sets custom CSS styles for the Experience Details section in Streamlit."""
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
    .experience-entry {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .experience-entry h2 {
        font-size: 30px;
        color: #444;
        text-align: center;
        font-weight: bold;
    }
    .experience-entry h3 {
        font-size: 20px;
        color: #444;
        margin-bottom: 8px;
    }
    .experience-entry h4 {
        font-size: 18px;
        color: #555;
        margin-bottom: 6px;
    }
    .separator {
        border: none;
        border-top: 2px solid #ddd;
        margin: 20px 0;
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
    .project-entry {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .project-entry h1 {
        font-size: 24px;
        color: #333;
        margin-bottom: 10px;
    }
    .project-entry h2 {
        font-size: 30px;
        color: #444;
        text-align: center;
        font-weight: bold;
    }
    .project-entry h3 {
        font-size: 18px;
        color: #555;
        margin-bottom: 6px;
    }
    .project-entry p {
        font-size: 16px;
        color: #666;
        line-height: 1.6em;
        text-align: left;
    }
    .project-entry ul {
        padding-left: 20px;
        margin-top: 10px;
    }
    .project-entry ul li {
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
