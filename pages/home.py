import streamlit as st

# Set page title


def app():
    # Define main content
    st.title("Welcome to the Ayurveda App!")
    st.write("Ayurveda is a traditional system of medicine that has its roots in India. It emphasizes a holistic approach to health and wellness, focusing on the balance of the mind, body, and spirit. Ayurveda has been practiced for thousands of years and continues to be an important part of healthcare in many parts of the world.")

    # Add images
    st.image("pages/ashwagandha.jpg", use_column_width=True)
    # st.image("ayurveda2.jpg", use_column_width=True)

    st.header("Our Services")
    st.write("Our Ayurveda app provides a range of services, including:")

    # List of services
    services = [
        "Disease diagnosis based on symptoms",
        "Herbal remedies for common ailments",
        "Ayurvedic lifestyle and wellness advice",
        "Ayurvedic Quiz for Knowing Your Dosha",
        "Charak Samhita Info extracted"
    ]

    for service in services:
        st.write("- " + service)


    # Define footer content
   # st.write("Made with ❤️")
