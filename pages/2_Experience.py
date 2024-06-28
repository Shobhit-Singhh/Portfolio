import streamlit as st
from utils.get_footer import get_footer
from utils.css_styling import experience_custom_style
from data.params.experiences import experience_details


def display_experience_entry(experience_title, details):
    """Display individual experience entry."""
    st.markdown(f'<div class="experience-entry"><h2>{experience_title}</h2>', unsafe_allow_html=True)  # Experience title
    
    projects = details.get("Projects", {})
    responsibilities = details.get("Responsibilities", {})
    
    for project_title, project_summary in projects.items():
        st.markdown(f'<h3>Project: {project_title}</h3>', unsafe_allow_html=True)
        for summary in project_summary:
            st.write("- " + summary)
    
    st.markdown('<hr class="separator"/>', unsafe_allow_html=True)  # Custom styled separator
    
    col1, col2 = st.columns(2)
    responsibility_titles = list(responsibilities.keys())
    half_index = len(responsibility_titles) // 2
    
    with col2:
        for title in responsibility_titles[:half_index]:
            st.markdown(f'<h3>{title}</h3>', unsafe_allow_html=True)
            for detail in responsibilities[title]:
                st.write("- " + detail)

    with col1:
        for title in responsibility_titles[half_index:]:
            st.markdown(f'<h3>{title}</h3>', unsafe_allow_html=True)
            for detail in responsibilities[title]:
                st.write("- " + detail)

    st.markdown('<hr class="separator"/>', unsafe_allow_html=True)  # Custom styled separator


def display_thesis_entry(thesis_title, details):
    """Display thesis project entry."""
    st.markdown(f'<div class="experience-entry"><h2>{thesis_title}</h2>', unsafe_allow_html=True)  # Thesis title

    st.markdown(f"<h3>Institute: {details['Institute']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3>Specialisation: {details['Specialisation']}</h3>", unsafe_allow_html=True)

    for section_title, section_content in details["Project"].items():
        if section_title == "Key Components" or section_title == "Benefits":
            st.markdown(f'<h3>{section_title}</h3>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            items = list(section_content.items())
            half_index = len(items) // 2
            with col2:
                for title, content in items[:half_index]:
                    st.markdown(f'<h4>{title}</h4>', unsafe_allow_html=True)
                    st.write("- " + content)
            with col1:
                for title, content in items[half_index:]:
                    st.markdown(f'<h4>{title}</h4>', unsafe_allow_html=True)
                    st.write("- " + content)
        else:
            st.markdown(f'<h3>{section_title}</h3>', unsafe_allow_html=True)
            st.write(section_content)

    st.markdown('<hr class="separator"/>', unsafe_allow_html=True)  # Custom styled separator

def sidebar():
    # in sidebar i want to add my photo 
    st.sidebar.image("data/images/shobhit.jpg", use_column_width=True)
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
            <h2>Shobhit Kumar Singh</h2>
            <p style="font-style: italic;">Senior Executive Data Scientist</p>
            <p>I'm passionate about AI and data analysis. Seeking opportunities to contribute to innovative projects.</p>
        </div>
        """,
        unsafe_allow_html=True
    )



def main():
    """Main function to display experience and thesis project."""
    experience_custom_style()

    experiences = experience_details()
    st.title("Experience")
    
    for category, entries in experiences.items():
        st.markdown(f'<h2>{category}</h2>', unsafe_allow_html=True)
        for title, details in entries.items():
            if category == "M.Tech Thesis Project":
                display_thesis_entry(title, details)
            else:
                display_experience_entry(title, details)


if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="My Experiences",
        page_icon=":briefcase:",
    )
    sidebar()
    main()
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)