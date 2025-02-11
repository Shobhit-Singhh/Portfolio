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

def sidebar():
    # in sidebar i want to add my photo 
    st.sidebar.image("data/images/shobhit.jpg", use_container_width=True)
    st.markdown(
        """
        <style>
        .sidebar-section {
            text-align: center;
            margin-bottom: 30px;
        }
        .sidebar-image {
            border-radius: 50%;
            width: 150px; /* Adjust size as needed */
            height: 150px; /* Adjust size as needed */
            object-fit: cover;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Sidebar content
    st.sidebar.markdown(
        """
        <div class="sidebar-section">
            <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="large" data-theme="dark" data-type="HORIZONTAL" data-vanity="shobhit-singhh" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/shobhit-singhh?trk=profile-badge">Shobhit Singh</a></div>
            <p style="font-style: italic;">Senior Executive Data Scientist</p>
            <p>I'm passionate about AI and data analysis. Seeking opportunities to contribute to innovative projects.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    st.set_page_config(layout="wide", page_icon="🌟")
    sidebar()
    main()
    
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
