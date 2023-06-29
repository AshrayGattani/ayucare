import streamlit as st

# Set page title
def app():
    # st.title("Ayurvedic Dosha Quiz")

    # Define quiz questions and options
    questions = {
        "Q1": "What is your body frame like?",
        "Q2": "What is your skin type like?",
        "Q3": "What is your appetite like?",
        "Q4": "What is your energy level like?",
        "Q5": "Which word describes you best?",
        "Q6": "How do you react to stress?",
        "Q7": "What is your preferred food taste?",
        "Q8": "What is your preferred time of the day?"
    }

    options = {
        "Q1": ["Small and light", "Medium and balanced", "Large and heavy"],
        "Q2": ["Dry and rough", "Sensitive and fair", "Oily and thick"],
        "Q3": ["Irregular", "Strong and consistent", "Low and slow"],
        "Q4": ["High and active", "Moderate and steady", "Low and lethargic"],
        "Q5": ["Active", "Ambitious", "Calm"],
        "Q6": ["Anxious","Irritable","Withdrawn"],
        "Q7": ["Sweet, sour, and salty","Spicy, salty, and pungent","Bitter, acidic, and sweet"],
        "Q8": ["Morning","Noon","Evening"]
    }

    # Define Dosha descriptions and properties
    doshas = {
        "Vata": {
            "Description": "Vata is characterized by the elements of air and space. It is associated with creativity, movement, and change.",
            "Properties": ["Dry", "Light", "Cold", "Rough"],
        },
        "Pitta": {
            "Description": "Pitta is characterized by the elements of fire and water. It is associated with digestion, metabolism, and transformation.",
            "Properties": ["Hot", "Sharp", "Light", "Oily"],
        },
        "Kapha": {
            "Description": "Kapha is characterized by the elements of earth and water. It is associated with stability, structure, and lubrication.",
            "Properties": ["Heavy", "Slow", "Cool", "Smooth"],
        },
    }

    # Define main content
    st.title("Ayurvedic Dosha Quiz")
    st.write("Discover your Ayurvedic Dosha by answering the following questions.")

    # Define quiz function


    def run_quiz(questions, options, doshas):
        dosha_scores = {
            "Vata": 0,
            "Pitta": 0,
            "Kapha": 0,
        }
        for q_num, question in questions.items():
            selected_option = st.selectbox(question, options[q_num])
            if selected_option == options[q_num][0]:
                dosha_scores["Vata"] += 1
            elif selected_option == options[q_num][1]:
                dosha_scores["Pitta"] += 1
            elif selected_option == options[q_num][2]:
                dosha_scores["Kapha"] += 1
        max_dosha = max(dosha_scores, key=dosha_scores.get)
        st.subheader("Your Ayurvedic Dosha is: " + max_dosha)
        st.write(doshas[max_dosha]["Description"])
        st.write("Properties: " + ", ".join(doshas[max_dosha]["Properties"]))


    # Run quiz function
    run_quiz(questions, options, doshas)

    # Define footer content
    # st.write("Made with ❤️")
