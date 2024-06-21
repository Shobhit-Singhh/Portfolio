import streamlit as st
from utils.get_footer import get_footer
from utils.css_styling import education_custom_style
from data.params.education import education_details

def display_education_entry(degree, custom_line=""):
    """Displays a formatted education entry with a friendly message and custom line."""
    st.write(f"<div class='education-entry'><div class='degree-name'>{degree} :</div>", unsafe_allow_html=True)
    
    st.write(f"<div class='degree-message'>{custom_line}</div></div>", unsafe_allow_html=True)
    st.write("")  # Add an empty line for spacing

def main():
    """Main function to display educational background."""
    education_custom_style()  # Use the new CSS styling function
    st.title("My Education")

    # Get education dictionary
    education = education_details()

    # Loop through education details and display them
    for category_title, degree_dict in education.items():
        st.header(category_title)
        for degree, (_, custom_line) in degree_dict.items():
            display_education_entry(degree, custom_line)
        st.markdown("---")

if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="My Education",
        page_icon=":mortar_board:",
    )
    main()
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
