import streamlit as st
from utils.get_footer import get_footer
from utils.css_styling import technical_skill_custom_style
from data.params.skills import technical_skills

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


def display_skill_progress(skill, completion, custom_line=""):
    """Displays a progress bar for a specific skill with a friendly message and custom line."""
    st.markdown(f"### <div class='skill-category'>{skill}", unsafe_allow_html=True)

    # st.markdown(f"<div class='skill-entry'><div class='skill-name'>{} :</div>", unsafe_allow_html=True)
    
    # Create a horizontal layout with columns
    col1, col2 = st.columns([9, 1])  # Adjust the ratio to control the width of the columns
    with col1:
        st.progress(completion)
    with col2:
        st.write(f"<div class='skill-percentage'>{int(completion * 100)}%</div>", unsafe_allow_html=True)
    
    progress_message = f"{custom_line}" if custom_line else f"I mastered {completion * 100:.0f}% of {skill}!"
    st.write(f"<div class='skill-message'>{progress_message}</div></div>", unsafe_allow_html=True)
    st.write("")  # Add an empty line for spacing


def main():
    """Main function to display technical skills."""
    technical_skill_custom_style()
    st.title("My Technical Skills")
    st.markdown("Here are some of the technical skills I have acquired through my academic studies, personal projects, and work experience.")

    # Get skills dictionary
    skills = technical_skills()

    # Loop through skills and display them
    for category_title, skill_dict in skills.items():
        st.markdown(f"<div class='skill-entry'><div class='skill-name'>{category_title} :</div class='skill-name>", unsafe_allow_html=True)
        # st.markdown(f"<div class='skill-category'><h1>{category_title}</h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        for i, (skill, (completion, custom_line)) in enumerate(skill_dict.items()):
            if i % 2 == 0:
                with col1:
                    display_skill_progress(skill, completion, custom_line)
            else:
                with col2:
                    display_skill_progress(skill, completion, custom_line)
        st.markdown("---")


if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_title="My Portfolio",
        page_icon=":trophy:",
    )
    sidebar()
    main()
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
