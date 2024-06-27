import json
import streamlit as st
from utils.get_footer import get_footer
from streamlit-streamlit-lottie import st_lottie

def lottie(path: str):
    with open(path) as f:
        return json.load(f)


def main():
    st.title("Welcome to My Portfolio")
    st.write("""
    This is where you can showcase your projects, experiences, and skills.
    """)

    # Display your projects
    st.header("Projects")
    st.write("""
    Here are some of my recent projects:
    - Project 1: Description of Project 1
    - Project 2: Description of Project 2
    """)

    # Display your experiences
    st.header("Experiences")
    st.write("""
    - Data Science Intern at Primary Healthtech Private Limited
      - Utilized clinical trial data for process optimization.
      - Improved accuracy by 30% and precision by 25% of diagnostic device.
      - Optimized reaction parameters to reduce testing time by 50%.
    """)

    # Display your skills
    st.header("Skills")
    st.write("""
    - Python, SQL, Machine Learning, Data Visualization
    - Streamlit, HTML/CSS, JavaScript
    """)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="My Portfolio", page_icon="🌟")
    main()

    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
