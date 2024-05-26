import streamlit as st
from utils.get_footer import get_footer

def display_skill_progress(skill, completion, custom_line=""):
    """Displays a progress bar for a specific skill with a friendly message and custom line."""
    # Display the skill name
    st.write(f"<div style='margin: 0; padding: 0; font-size: larger; font-weight: bold;'>{skill}</div>", unsafe_allow_html=True)

    # Create a horizontal layout with columns
    col1, col2 = st.columns([9, 1])  # Adjust the ratio to control the width of the columns
    with col1:
        st.progress(completion)  
    with col2:
        st.write(f"<div style='text-align: left; padding-top: 10px;'>{int(completion * 100)}%</div>", unsafe_allow_html=True)
    progress_message = f"{custom_line}" if custom_line else f"I mastered {completion * 100:.0f}% of {skill}!"
    st.write(f"<div style='margin: 0; padding: 0; font-size: small; font-style: italic;'>{progress_message}</div>", unsafe_allow_html=True)
    st.write("")  # Add an empty line for spacing

def main():
    """Displays your technical skills in a user-friendly and visually appealing way."""
    st.title("My Technical Skills")
    st.markdown("Here are some of the technical skills I have acquired through my academic studies, personal projects, and work experience. ")  


    skills = {
        "Languages": {
            "C/C++": (1.0, "Developed a proficient understanding of C++ during my secondary school education as part of my curriculum."),
            "Python": (1.0, "Utilized Python extensively for data analysis and machine learning in my master's thesis."),
            "SQL": (0.8, "Gained comprehensive understanding of SQL through coursework in Database Management Systems."),
            "MATLAB": (0.5, "Applied MATLAB in various academic assignments and projects."),
        },

        "Deployment": {
            "Machine Learning": (0.9, "Deployed multiple machine learning models in various projects, demonstrating practical proficiency."),
            "Artificial Neural Networks": (0.85, "Presented a case study on crime rate prediction, comparing ANNs with other machine learning models."),
            "Convolutional Neural Networks": (0.8, "Developed a skin cancer detection and classification model using CNN architectures such as VGG16 and ResNet50."),
            "Recurrent Neural Networks": (0.5, "Acquired a theoretical understanding of RNNs and their applications."),
            "Natural Language Processing": (0.8, "Executed sentiment analysis and text classification projects using NLP techniques."),
            "Large Language Models": (0.7, "Implemented a question-answering system using BERT, fine-tuning it on the SQuAD dataset."),
        },

        "Frameworks": {
            "Streamlit": (1.0, "Built a comprehensive data analysis and machine learning web application using Streamlit."),
            "Tkinter": (0.8, "Developed a GUI for a project to interface with Arduino and display sensor data."),
            "FastAPI": (0.7, "Created a simple and efficient API using FastAPI."),
            "LangChain": (0.6, "Developed a basic chatbot leveraging LangChain framework."),
        },

        "Databases": {
            "MySQL": (0.9, "Designed and managed multiple databases and tables in MySQL."),
            "MongoDB": (0.7, "Created and managed a basic database using MongoDB."),
        },

        "MLOps": {
            "Git": (0.8, "Utilized Git for version control across numerous projects."),
            "Docker": (0.8, "Containerized machine learning models using Docker for deployment."),
            "Kubernetes": (0.7, "Deployed machine learning models using Kubernetes for scalable solutions."),
            "MLflow": (0.7, "Employed MLflow for tracking and managing machine learning experiments."),
            "TensorBoard": (0.7, "Used TensorBoard for visualizing the performance of machine learning models."),
            "DVC": (0.8, "Applied DVC for version control and management of machine learning models."),
        },
        
        "Libraries": {
            "Pandas": (0.9, "Extensively used Pandas for data manipulation and analysis in various data science projects."),
            "NumPy": (0.9, "Leveraged NumPy for numerical computing in machine learning and data analysis tasks."),
            "Matplotlib": (0.8, "Generated static visualizations for academic reports and data presentations using Matplotlib."),
            "Seaborn": (0.8, "Created statistical graphics for data visualization projects using Seaborn."),
            "Plotly": (0.8, "Developed interactive visualizations for web applications and dashboards using Plotly."),
            "Scikit-learn": (0.9, "Implemented machine learning algorithms using Scikit-learn in multiple projects, including my master's thesis."),
            "TensorFlow": (0.9, "Built deep learning models with TensorFlow for projects like image classification and NLP."),
            "NLTK": (0.7, "Processed and analyzed text data for a sentiment analysis project using NLTK."),
            "spaCy": (0.7, "Used spaCy for various NLP tasks in a text classification project."),
            "Hugging Face Transformers": (0.7, "Fine-tuned models for NLP tasks, including question-answering systems and chatbots, using Hugging Face Transformers."),
        },

        "Dashboarding": {
            "Tableau": (0.8, "Designed interactive dashboards for data visualization during my internship at a health data analytics company."),
            "Power BI": (0.7, "Developed analytics dashboards for an inventory control system project using Power BI."),
        },

        "Miscellaneous": {
            "Data Structures and Algorithms": (0.9, "Established a strong foundation in data structures and algorithms through coursework and competitive programming."),
            "Object-Oriented Programming": (0.9, "Applied OOP principles in various projects, including automation and machine learning model implementation."),
            "Functional Programming": (0.8, "Gained experience in functional programming paradigms through coursework and algorithm implementation in Python."),
            "Software Design Patterns": (0.8, "Applied common design patterns in software development projects."),
            "RESTful APIs": (0.8, "Developed APIs adhering to REST architecture for web applications and machine learning model deployment."),
            "Web Scraping": (0.8, "Conducted data extraction from websites using Python for market research and data collection projects."),
            "Regular Expressions": (0.7, "Utilized regular expressions for pattern matching and text data extraction in multiple projects."),
        }
    }


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
        page_icon="",
    )

    main()
    footer = get_footer()
    st.markdown(footer, unsafe_allow_html=True)
