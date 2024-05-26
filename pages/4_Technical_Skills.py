import streamlit as st
from utils.get_footer import get_footer
from utils.css_styling import technical_skill_custom_style
from data.params.skills import technical_skills

def display_skill_progress(skill, completion, custom_line=""):
    """Displays a progress bar for a specific skill with a friendly message and custom line."""
    st.write(f"<div class='skill-entry'><div class='skill-name'>{skill} :</div>", unsafe_allow_html=True)
    
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
        st.header(category_title)
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
    main()
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
