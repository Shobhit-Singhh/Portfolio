import streamlit as st
from utils.get_footer import get_footer
from utils.css_styling import project_custom_style
from data.params.projects import project_details 

def display_project_entry(project_title, details):
    """Display individual project entry."""
    st.markdown(f'### <div class="project-entry"><h2>{project_title}</h2>', unsafe_allow_html=True)  # Start of project entry
        
    for key, value in details.items():
        if isinstance(value, list):
            # st.markdown(f'<div class="project-box-content">', unsafe_allow_html=True)  # Start of project content
            st.subheader(key)
            for item in value:
                st.write("- " + item)
            st.markdown('</div>', unsafe_allow_html=True)  # End of project content
        else:
            # st.markdown(f'<div class="project-box-content">', unsafe_allow_html=True)  # Start of project content
            st.subheader(key)
            st.write("- " + value)
            st.markdown('</div>', unsafe_allow_html=True)  # End of project content
    
    st.markdown('</div>', unsafe_allow_html=True)  # End of project entry



def main():
    """Main function to display project details."""
    project_custom_style()  # Apply custom CSS styling
    st.title("My Projects")

    projects = project_details()  # Fetch project details from data source

    project_titles = [project_title for category in projects.values() for project_title in category.keys()]
    selected_project = st.selectbox("Select a project", project_titles)

    for category_title, category_projects in projects.items():
        for project_title, details in category_projects.items():
            if project_title == selected_project:
                display_project_entry(project_title, details)

if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="My Projects",
        page_icon=":rocket:",  # Set page icon
    )
    main()  # Run the main function to display projects
    footer = get_footer()  # Fetch footer content
    st.markdown(footer, unsafe_allow_html=True)  # Display footer content
