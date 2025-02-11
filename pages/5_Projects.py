import streamlit as st
from utils.get_footer import get_footer
from utils.css_styling import project_custom_style
from data.params.projects import project_details 

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


def display_project_entry(project_title, details):
    """Display individual project entry."""
    st.markdown(f'### <div class="project-entry"><h2>{project_title}</h2>', unsafe_allow_html=True)  # Start of project entry
        
    for key, value in details.items():
        if isinstance(value, list):
            st.subheader(key)
            for item in value:
                st.write("- " + item)
            st.markdown('</div>', unsafe_allow_html=True)  # End of project content
        elif "Role" in key:
            st.subheader(key + ": " + value)
            
        else:
            st.subheader(key)
            st.write(value)
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
    sidebar()
    main()  # Run the main function to display projects
    footer = get_footer()  # Fetch footer content
    st.markdown(footer, unsafe_allow_html=True)  # Display footer content
