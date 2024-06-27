import streamlit as st
from utils.get_footer import get_footer
from utils.css_styling import education_custom_style
from data.params.education import education_details

def display_education_entry(degree_title, details):
    """Display individual education entry."""
    st.markdown(f'<div class="degree-entry"><h2>{degree_title}</h2></div>', unsafe_allow_html=True)  # Degree title
    
    for key, value in details.items():
        if isinstance(value, list):
            st.subheader(key)
            for item in value:
                st.write("- " + item)
        elif "Specialisation" in key or "Major" in key or "CGPA" in key or "Percentage" in key:
            st.subheader(key +": "+ value)
            
        else:
            st.subheader(key)
            st.write(value)
    st.markdown('<hr class="custom-separator">', unsafe_allow_html=True)  # Aesthetically pleasing separator

def main():
    """Main function to display education details."""
    education_custom_style()  
    st.title("My Education")

    educations = education_details()

    for category, entries in educations.items():
        st.markdown(f'<h2>{category}</h2>', unsafe_allow_html=True)
        for degree_title, details in entries.items():
            display_education_entry(degree_title, details)

if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="My Education",
        page_icon=":mortar_board:",
    )
    main()
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
