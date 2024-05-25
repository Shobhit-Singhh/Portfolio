import streamlit as st

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
            "C/C++": (1.0, "I opted for C++ as a subject during my secondary school education, resulting in a proficient understanding of the language."),
            "Python": (1.0, "In my master's thesis, I used Python for data analysis and machine learning."),
            "SQL": (0.8, "I have DBMS in my course curriculum, which has provided me with a comprehensive understanding of SQL."),
            "MATLAB": (0.5, "I have used MATLAB for my academic assignments."),
        },

        "Deployment": {
            "Machine Learning": (0.9, "I have learned and deployed multiple machine learning models in a couple of projects."),
            "Artificial Neural Networks": (0.85, "I compared the performance of ANNs with other machine learning models and presented a case study on a crime rate dataset."),
            "Convolutional Neural Networks": (0.8, "I have worked on a skin cancer detection and classification model using CNNs like VGG16 and ResNet50."),
            "Recurrent Neural Networks": (0.5, "I have a theoretical understanding of RNNs and their applications."),
            "Natural Language Processing": (0.75, "I have worked on sentiment analysis and text classification using NLP."),
            "Large Language Models": (0.7, "I have worked on a question-answering system using BERT and fine-tuned it on the SQuAD dataset."),
        },

        "Frameworks": {
            "Streamlit": (1.0, "I built an end-to-end data analysis and machine learning web application using Streamlit."),
            "Tkinter": (0.8, "I created a GUI for a project to communicate with Arduino and generate sensor data."),
            "FastAPI": (0.7, "I have created a simple API using FastAPI."),
            "LangChain": (0.6, "I have created a simple chatbot using LangChain."),
        },

        "Databases": {
            "MySQL": (0.9, "I have created multiple databases and tables in MySQL."),
            "MongoDB": (0.7, "I have created a simple database in MongoDB."),
        },

        "MLOps": {
            "Git": (0.9, "I have used Git for version control in multiple projects."),
            "Docker": (0.8, "I have containerized my machine learning models using Docker."),
            "Kubernetes": (0.7, "I have deployed my machine learning models on Kubernetes."),
            "MLflow": (0.7, "I have used MLflow for tracking and managing machine learning experiments."),
            "TensorBoard": (0.7, "I have used TensorBoard for visualizing machine learning models."),
            "DVC": (0.6, "I have used DVC for versioning and managing machine learning models."),
        },
        
        "Libraries": {
            "Pandas": (0.9, "I used Pandas extensively for data manipulation and analysis in my various data science projects."),
            "NumPy": (0.9, "I utilized NumPy for numerical computing in numerous machine learning and data analysis tasks."),
            "Matplotlib": (0.8, "I created various static visualizations for academic reports and data presentations using Matplotlib."),
            "Seaborn": (0.8, "I built statistical graphics on top of Matplotlib for data visualization projects."),
            "Plotly": (0.8, "I developed interactive visualizations for web applications and dashboards using Plotly."),
            "Scikit-learn": (0.9, "I applied machine learning algorithms using Scikit-learn in multiple projects, including my master's thesis."),
            "TensorFlow": (0.9, "I implemented deep learning models using TensorFlow for several projects, such as image classification and NLP."),
            "NLTK": (0.7, "I processed and analyzed text data using NLTK for a sentiment analysis project."),
            "spaCy": (0.7, "I used spaCy for natural language processing tasks in a text classification project."),
            "Hugging Face Transformers": (0.7, "I worked on NLP tasks using Hugging Face Transformers, including fine-tuning models for question-answering systems and chatbots."),
        },

        "Dashboarding": {
            "Tableau": (0.8, "I created interactive dashboards for data visualization in my internship at a health data analytics company."),
            "Power BI": (0.7, "I used Power BI to develop analytics dashboards for a project on inventory control system in my company."),
        },

        "Miscellaneous": {
            "Data Structures and Algorithms": (0.9, "I have a strong foundation in data structures and algorithms from my coursework and competitive programming."),
            "Object-Oriented Programming": (0.9, "I applied OOP principles in various projects, including automation project and machine learning model implementation."),
            "Functional Programming": (0.8, "I gained experience with functional programming paradigms during my coursework and through implementing algorithms in Python."),
            "Software Design Patterns": (0.8, "I am familiar with common design patterns and have applied them in software development projects."),
            "RESTful APIs": (0.8, "I built APIs conforming to REST architecture for web applications and machine learning model deployment."),
            "Web Scraping": (0.8, "I extracted data from websites using Python for a project on market research and data collection."),
            "Regular Expressions": (0.7, "I used regular expressions for pattern matching and text data extraction in multiple projects."),
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
