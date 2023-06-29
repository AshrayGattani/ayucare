import streamlit as st

# Define the questions and answer options
def app():

    questions = [
        {
            "question": "How would you describe your body shape?",
            "options": ["Thin", "Average", "Solid"],
        },
        {
            "question": "Do you tend to gain or lose weight easily?",
            "options": ["Struggle to gain weight", "Maintain weight easily", "Tend to gain weight easily"],
        },
        {
            "question": "How is your appetite?",
            "options": ["Variable", "Strong", "Steady"],
        },
        {
            "question": "Do you prefer warm or cold weather?",
            "options": ["Prefer warmth", "Prefer cooler temperatures", "No strong preference"],
        },
        {
            "question": "How do you handle stress?",
            "options": ["Anxious or worried", "Irritable or angry", "Calm and composed"],
        },
        {
            "question": "How is your digestion?",
            "options": ["Tendency for gas or bloating", "Strong digestion, prone to heartburn", "Slow digestion, can gain weight easily"],
        }
    ]

    # Initialize the dosha scores
    vata_score = 0
    pitta_score = 0
    kapha_score = 0

    # Display the quiz
    st.title("Discover Your Dosha")

    for i, question in enumerate(questions):
        st.header(f"Question {i+1}")
        st.write(question["question"])
        
        # Display the answer options
        selected_option = st.radio("Select your answer:", question["options"])
        
        # Update dosha scores based on the selected option
        if selected_option == question["options"][0]:
            vata_score += 1
        elif selected_option == question["options"][1]:
            pitta_score += 1
        elif selected_option == question["options"][2]:
            kapha_score += 1

    # Determine the predominant dosha
    dosha_scores = {"Vata": vata_score, "Pitta": pitta_score, "Kapha": kapha_score}
    predominant_dosha = max(dosha_scores, key=dosha_scores.get)

    # Display the dosha results
    st.header("Dosha Results")
    st.write(f"Your predominant dosha is: {predominant_dosha}")
