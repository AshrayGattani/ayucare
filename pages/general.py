import streamlit as st
from pages import quiz
# import your pages here
# import your pages here
# Create an instance of the app


# Define dosha-specific lifestyle advice
lifestyle_advice = {
    "Vata": {
        "diet": ["Eat warm, cooked foods", "Avoid cold or raw foods", "Drink warm beverages"],
        "exercise": ["Choose low-impact exercises", "Practice grounding activities like yoga or walking"],
        "sleep": ["Maintain a regular sleep schedule", "Use calming scents like lavender or chamomile"],
        "stress_management": ["Practice mindfulness or meditation", "Reduce exposure to loud or chaotic environments"],
        "general_health": ["Stay warm and protected from the elements", "Establish a consistent self-care routine"]
    },
    "Pitta": {
        "diet": ["Eat cooling foods like cucumber or coconut", "Avoid spicy or acidic foods", "Drink plenty of water"],
        "exercise": ["Engage in moderate exercise like jogging or cycling", "Avoid intense workouts during peak heat hours"],
        "sleep": ["Maintain a regular sleep schedule", "Use cooling scents like sandalwood or mint"],
        "stress_management": ["Practice calming activities like swimming or reading", "Avoid confrontational situations"],
        "general_health": ["Stay cool and protected from the sun", "Take breaks to rest and recharge throughout the day"]
    },
    "Kapha": {
        "diet": ["Eat light, easily-digestible foods", "Avoid heavy or oily foods", "Drink warm, stimulating beverages"],
        "exercise": ["Engage in vigorous exercise like running or weightlifting", "Avoid sedentary activities"],
        "sleep": ["Maintain a regular sleep schedule", "Use invigorating scents like eucalyptus or citrus"],
        "stress_management": ["Stay active and engaged with the world", "Avoid prolonged periods of inactivity or boredom"],
        "general_health": ["Stay active and motivated", "Incorporate variety and new experiences into your routine"]
    }
}


def app():


    def lifestyleadvice():
        # Display title and description
        st.title("Ayurvedic Lifestyle Advice")
        st.write(
            "Answer a few questions about yourself to receive personalized Ayurvedic lifestyle advice.")

        # Collect user input for dominant dosha
        st.header("Step 1: Identify Your Dominant Dosha")
        st.write("Take a quiz")
        dosha_options = ["Vata", "Pitta", "Kapha"]
        dominant_dosha = st.selectbox(
            "Select your dominant dosha:", dosha_options)
        # Display lifestyle advice for selected dosha
        st.header("Step 2: Review Your Lifestyle Advice")
        st.write(
            "Based on your dominant dosha, here are some lifestyle tips to help you achieve balance:")
        st.subheader("Diet")
        for tip in lifestyle_advice[dominant_dosha]["diet"]:
            st.write("- " + tip)
        st.subheader("Exercise")
        for tip in lifestyle_advice[dominant_dosha]["exercise"]:
            st.write("- " + tip)
        st.subheader("Sleep")
        for tip in lifestyle_advice[dominant_dosha]["sleep"]:
            st.write("- " + tip)
        st.subheader("Stress Management")
        for tip in lifestyle_advice[dominant_dosha]["stress_management"]:
            st.write("- " + tip)
        st.subheader("Overall Health")
        for tip in lifestyle_advice[dominant_dosha]["general_health"]:
            st.write("- " + tip)
    
    lifestyleadvice()

