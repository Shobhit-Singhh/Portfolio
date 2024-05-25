import streamlit as st
from utils.get_footer import get_footer
import pdfplumber


def main():
    pass


def display_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            st.image(page.to_image(resolution=300).original)

def main():
    resume_path = 'data/Shobhit_resume.pdf' 
    display_pdf(resume_path)

    
    with open(resume_path, 'rb') as file:
        pdf_bytes = file.read()

    # Add the download button
    st.download_button(
        label="Download Resume",
        data=pdf_bytes,
        file_name="Shobhit_resume.pdf",
        mime="application/pdf"
    )

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_icon="🌟")
    main()
    
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
