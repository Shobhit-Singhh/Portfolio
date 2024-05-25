import streamlit as st
from utils.get_footer import get_footer

def main():
    pass

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="My Portfolio", page_icon="🌟")
    main()
    
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)