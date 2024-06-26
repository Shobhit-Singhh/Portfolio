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

    with col1:
        for title in responsibility_titles[half_index:]:
            st.markdown(f'<h3>{title}</h3>', unsafe_allow_html=True)
            for detail in responsibilities[title]:
                st.write("- " + detail)

    with col2:
        for title in responsibility_titles[:half_index]:
            st.markdown(f'<h3>{title}</h3>', unsafe_allow_html=True)
            for detail in responsibilities[title]:
                st.write("- " + detail)

    st.markdown('<hr class="separator"/>', unsafe_allow_html=True)  # Custom styled separator

def display_thesis_entry(thesis_title, details):
    """Display thesis project entry."""
    st.markdown(f'<div class="experience-entry"><h2>{thesis_title}</h2>', unsafe_allow_html=True)  # Thesis title

    st.markdown(f"<h3>Institute:</h3> {details['Institute']}", unsafe_allow_html=True)
    st.markdown(f"<h3>Specialisation:</h3> {details['Specialisation']}", unsafe_allow_html=True)

    for section_title, section_content in details["Project"].items():
        st.markdown(f'<h3>{section_title}</h3>', unsafe_allow_html=True)
        st.write(section_content)

    st.markdown('<hr class="separator"/>', unsafe_allow_html=True)  # Custom styled separator

def main():
    """Main function to display experience and thesis details."""
    experience_custom_style()
    st.title("My Experiences")

    experiences = experience_details()
    
    for category, entries in experiences.items():
        st.header(category)
        for title, details in entries.items():
            if category == "Thesis Project Experience":
                display_thesis_entry(title, details)
            else:
                display_experience_entry(title, details)

if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="My Experiences",
        page_icon=":briefcase:",  
    )
    main()
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
