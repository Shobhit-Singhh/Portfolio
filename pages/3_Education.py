import streamlit as st
from utils.get_footer import get_footer
from utils.css_styling import education_custom_style
from data.params.education import education_details

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
    sidebar()
    main()
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
