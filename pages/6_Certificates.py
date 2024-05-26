# main.py
import streamlit as st
from utils.get_footer import get_footer
from data.params.certificate import certificate
from utils.css_styling import certificate_custom_css

def display_certificates(certificates):
    """Displays certificates in a visually appealing format."""
    # Create two columns for a responsive layout
    col1, col2 = st.columns(2)
    
    for i, certificate in enumerate(certificates):
        # Determine which column to use
        col = col1 if i % 2 == 0 else col2
        
        with col:
            st.image(certificate["image"], use_column_width=True)  # Adjust image to fit column width
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
    main()
    
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
