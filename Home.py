import json
import streamlit as st
from utils.get_footer import get_footer
from streamlit_lottie import st_lottie

def lottie(path: str):
    with open(path) as f:
        return json.load(f)

# Load custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    load_css("utils/home.css")
    st.title("Shobhit Kumar Singh")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.header("Welcome to My Portfolio")
        st.header("About Me")
        st.write("""
        Reflecting on my journey, taking that leap of faith from mechanical engineering into the vibrant worlds of Artificial Intelligence and data analysis was one of the most pivotal decisions of my life. The path has been nothing short of rewarding. Delving into these domains, I find myself continuously invigorated by the challenges and opportunities to apply my skills in innovative ways. My enthusiasm for AI has only grown, and as a Senior Executive Data Scientist, I take pride in my accomplishments.

        I've made a substantial impact in medical device manufacturing and clinical diagnostics by leveraging technology effectively. With my expertise in machine learning and advanced data analysis, coupled with a master's degree from IIT Guwahati, I'm enthusiastic about furthering innovation and excellence in the field.

        Beyond data analysis, I enjoy strength training, sketching, swimming, and capturing the beauty of the world through photography. I'm passionate about making a positive difference and look forward to embracing new opportunities for growth and impact! I thrive in collaborative environments where I can apply my skills to solve complex challenges and deliver impactful solutions.

        Feel free to explore my portfolio and get in touch if you're as passionate about data and innovation as I am. Let's connect and create something amazing together! I'm seeking opportunities to contribute my data science and artificial intelligence expertise to drive forward-thinking initiatives.
        """)
    with col2:
        st_lottie(lottie("data/gifs/home.json"), speed=2, key="stats_3_people", loop=True, width=600)

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="My Portfolio", page_icon="🌟")
    main()
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
