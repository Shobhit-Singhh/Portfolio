# main.py
import streamlit as st
from utils.get_footer import get_footer
from data.params.certificate import certificate
from utils.css_styling import certificate_custom_css

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


def display_certificates(certificates):
    """Displays certificates in a visually appealing format."""
    # Create two columns for a responsive layout
    col1, col2 = st.columns(2)
    
    for i, certificate in enumerate(certificates):
        # Determine which column to use
        col = col1 if i % 2 == 0 else col2
        
        with col:
            st.image(certificate["image"], use_container_width=True)  # Adjust image to fit column width
            st.markdown(f"""
            <div class="certificate-entry">
                <h3 class='title'>{certificate['title']}</h3>
                <p class='issuer'><em>Issued by: {certificate['issuer']}</em></p>
                <p class='link'><a href='{certificate['link']}' target='_blank'>Link to Certificate</a></p>
            </div>
            """, unsafe_allow_html=True)


def main():
    st.header("Coursera Certificates")
    st.markdown("Below are a few of the certificates i've achieved from various online platforms and courses.")
    certificate_custom_css()
    certificates = certificate()
    display_certificates(certificates)


if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="My Portfolio", page_icon=":trophy:")
    sidebar()
    main()
    
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)

