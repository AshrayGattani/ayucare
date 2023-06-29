import streamlit as st

# Define questions and options for quiz
questions = {
    "Q1": "What best describes your body type?",
    "Q2": "How does your skin feel?",
    "Q3": "What best describes your digestion?",
    "Q4": "How is your energy level throughout the day?",
}

options = {
    "Q1": ["Small and light", "Medium and balanced", "Large and heavy"],
    "Q2": ["Dry and rough", "Sensitive and fair", "Oily and thick"],
    "Q3": ["Irregular", "Strong and consistent", "Low and slow"],
    "Q4": ["High and active", "Moderate and steady", "Low and lethargic"],
}

# Define descriptions and lifestyle tips for each Dosha type
doshas = {
    "Vata": {
        "description": "Vata is characterized by qualities of air and space. People with a dominant Vata Dosha tend to be thin, have dry skin and hair, and may experience anxiety, worry, or insomnia.",
        "lifestyle_tips": ["Keep warm and avoid cold, dry, or raw foods", "Establish a regular routine and stick to it", "Engage in calming activities like meditation or yoga"]
    },
    "Pitta": {
        "description": "Pitta is characterized by qualities of fire and water. People with a dominant Pitta Dosha tend to have a medium build, fair skin, and a sharp mind, but may experience anger, irritability, or inflammation.",
        "lifestyle_tips": ["Stay cool and avoid spicy, fried, or acidic foods", "Take breaks to avoid overworking or overexertion", "Engage in cooling activities like swimming or hiking in nature"]
    },
    "Kapha": {
        "description": "Kapha is characterized by qualities of earth and water. People with a dominant Kapha Dosha tend to have a larger build, smooth skin, and a calm demeanor, but may experience sluggishness, depression, or weight gain.",
        "lifestyle_tips": ["Stay active and avoid heavy, oily, or sweet foods", "Incorporate more variety and stimulation in daily routine", "Engage in invigorating activities like dancing or jogging"]
    }
}

# Define function to run quiz


def run_quiz(doshas):
    st.title("Ayurvedic Quiz")
    st.write("Answer the following questions to determine your Dosha type:")

    # Set initial scores to 0 for each Dosha type
    dosha_scores = {
        "Vata": 0,
        "Pitta": 0,
        "Kapha": 0,
    }

    # Iterate through each question and update scores based on answers
    for question in questions:
        st.write(questions[question])
        answer = st.radio("", options[question])

        if answer == options[question][0]:
            dosha_scores["Vata"] += 1
        elif answer == options[question][1]:
            dosha_scores["Pitta"] += 1
        elif answer == options[question][2]:
            dosha_scores["Kapha"] += 1

    # Determine Dosha type based on scores
    max_score = max(dosha_scores.values())
    dosha_type = [k for k, v in dosha_scores.items() if v == max_score][0]

    st.write("Based on your quiz results, your Dosha type is: " + dosha_type)
    st.write(doshas[dosha_type]["description"])
def display_lifestyle_advice(doshas):
    st.title("Ayurvedic Lifestyle Advice")
    st.write("Based on your Dosha type, here are some lifestyle tips to help you achieve balance:")
# Retrieve Dosha type from quiz results
dosha_type = st.session_state["dosha_type"]

# Display lifestyle tips for corresponding Dosha type
for tip in doshas[dosha_type]["lifestyle_tips"]:
    st.write("- " + tip)
def main():
    st.set_page_config(page_title="Ayurvedic App", page_icon="🌿")
    st.sidebar.title("Navigation")
    page_options = ["Home", "Ayurvedic Quiz", "Lifestyle Advice"]
    page = st.sidebar.radio("", page_options)
