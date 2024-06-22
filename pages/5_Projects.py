import streamlit as st
from utils.get_footer import get_footer
from utils.css_styling import project_custom_style
from data.params.projects import project_details 

def display_project_entry(project_title, details):
    """Display individual project entry."""
    st.markdown(f'<div class="project-box-header">{project_title}</div>', unsafe_allow_html=True)  # Project title
    
    # Loop through all keys in the details dictionary
    for key, value in details.items():
        if isinstance(value, list):
            st.subheader(key)
            for item in value:
                st.write("- " + item)
        else:
            st.subheader(key)
            st.write(value)


def main():
    """Main function to display project details."""
    project_custom_style()  
    st.title("My Projects")

    projects = project_details()

    project_titles = [project_title for category in projects.values() for project_title in category.keys()]
    selected_project = st.selectbox("Select a project", project_titles)

    for category_title, category_projects in projects.items():
        for project_title, details in category_projects.items():
            if project_title == selected_project:
                st.header(project_title)
                display_project_entry(project_title, details)

if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="My Projects",
        page_icon=":rocket:",  
    )
    main()
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
