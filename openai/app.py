import openai
import streamlit as st

# Set up OpenAI API credentials


# Define the OpenAI prompt that will be used to generate responses




openai.api_key = "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"
prompt = (
"Q: What are the diseases associated with {symptoms}? "
"A: The following diseases are associated with {symptoms}: [insert diseases].\n\n"
"Q: What are some Ayurvedic remedies for {disease}? "
"A: The following Ayurvedic remedies are recommended for {disease}: [insert remedies].\n\n"
)

# Define a function that uses the OpenAI API to generate responses
def generate_response(symptoms, disease):
    # Split the symptoms input into separate symptoms when commas are used as separators
    symptoms_list = [symptom.strip() for symptom in symptoms.split(",")]

    # Join the symptoms into a single string separated by "and" for use in the prompt
    symptoms_prompt = " and ".join(symptoms_list)

    # Generate a prompt with the given symptoms and disease
    prompt_with_symptoms_and_disease = prompt.format(symptoms=symptoms_prompt, disease=disease)

    # Use the OpenAI API to generate a response to the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_with_symptoms_and_disease,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()

    # Split the generated text into separate responses for each question
    responses = generated_text.split("\n\n")

    # Extract the diseases and remedies from the responses
    # diseases = responses[0].split(": ")[1].split(", ")
    # remedies = responses[1].split(": ")[1].split(", ")

    # Return the diseases and remedies as a tuple
    return responses
# Set the app title
st.title("Disease and Ayurvedic Remedy Generator")

# Create a text input for the user to enter their symptoms
symptoms = st.text_input("Enter your symptoms:")

# Create a text input for the user to enter a specific disease name
disease = st.text_input("Enter a specific disease (optional):")

# Generate responses when the user submits their symptoms and disease name
if st.button("Generate"):
    # diseases, remedies = generate_response(symptoms, disease)
    respon = generate_response(symptoms, disease)
    st.write(f"The following diseases are associated with {symptoms}:")
    # for disease in diseases:
    #     st.write(f"- {disease}")
    # st.write("")
    # st.write(f"The following Ayurvedic remedies are recommended for {disease}:")
    # for remedy in remedies:
    #     st.write(f"- {remedy}")
    st.write(respon)



