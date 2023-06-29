import streamlit as st

# Set page title
def app():
    

    # Define herbal remedies for common ailments
    remedies = {
        "Headache": ["Peppermint oil", "Feverfew", "Willow bark"],
        "Indigestion": ["Ginger", "Peppermint tea", "Chamomile tea"],
        "Stress and Anxiety": ["Lavender", "Chamomile", "Passionflower"],
        "Common Cold": ["Echinacea", "Ginger", "Honey"],
        "Insomnia": ["Valerian root", "Chamomile", "Lavender"],
        "Joint Pain": ["Turmeric", "Ginger", "Willow bark"],
    }

    # Define main content
    st.title("Herbal Remedies for Common Ailments")
    st.write("Explore natural and effective herbal remedies to relieve common ailments.")

    # Select ailment
    selected_ailment = st.selectbox(
        "Select an ailment to view herbal remedies", list(remedies.keys()))

    # Display herbal remedies for selected ailment
    st.header(selected_ailment)
    st.write("Here are some herbal remedies that may help with your " +
            selected_ailment.lower() + ":")

    for remedy in remedies[selected_ailment]:
        st.write("- " + remedy)

    # Define footer content
    # st.write("Made with ❤️")
