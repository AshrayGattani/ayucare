import streamlit as st

# Dictionary of sub-problems and their corresponding information and remedies
def app():

    sub_problems = {
        "Aggravation of Pitta Dosha": {
            "Information": "When vomiting is caused by an aggravation of Pitta Dosha, it is associated with symptoms such as burning sensation, acidity, and excessive heat in the body.",
            "Remedies": [
                "Chandana (Sandalwood)",
                "Sheetali (Cooling)",
                "Yashtimadhu (Licorice)"
            ]
        },
        "Food Poisoning": {
            "Information": "Vomiting caused by food poisoning is often accompanied by symptoms such as nausea, stomach cramps, and diarrhea.",
            "Remedies": [
                "Hingu (Asafoetida)",
                "Nimba (Neem)",
                "Guduchi (Tinospora Cordifolia)"
            ]
        },
        "Gastrointestinal Disorders": {
            "Information": "Gastrointestinal disorders like gastritis, gastric ulcers, or GERD can lead to frequent episodes of vomiting.",
            "Remedies": [
                "Patola (Pointed Gourd)",
                "Amalaki (Indian Gooseberry)",
                "Yashtimadhu (Licorice)"
            ]
        },
        "Emotional Disturbances": {
            "Information": "Emotional disturbances such as anxiety, stress, or depression can trigger vomiting episodes.",
            "Remedies": [
                "Brahmi (Bacopa Monnieri)",
                "Shankhapushpi (Convolvulus Pluricaulis)",
                "Jatamansi (Nardostachys Jatamansi)"
            ]
        },
        "Motion Sickness": {
            "Information": "Motion sickness can cause vomiting, especially during travel by car, boat, or airplane.",
            "Remedies": [
                "Ginger",
                "Ajwain (Carom Seeds)",
                "Shankhapushpi (Convolvulus Pluricaulis)"
            ]
        },
        "Migraine": {
            "Information": "Migraine headaches can be accompanied by nausea and vomiting as common symptoms.",
            "Remedies": [
                "Karpura (Camphor)",
                "Jatamansi (Nardostachys Jatamansi)",
                "Yashtimadhu (Licorice)"
            ]
        },
        # Add more sub-problems and their information and remedies
    }

    # Streamlit app layout
    st.title('Ayurvedic Remedies for Vomiting from Charaka Samhita')

    # Sub-problems dropdown
    sub_problem = st.selectbox('Select a sub-problem:', list(sub_problems.keys()))

    # Display the selected sub-problem information and remedies
    if sub_problem:
        information = sub_problems[sub_problem]["Information"]
        remedies = sub_problems[sub_problem]["Remedies"]
        
        st.subheader('Information:')
        st.write(information)

        st.subheader('Remedies:')
        for remedy in remedies:
            st.write('- ' + remedy)

        # Instructions on how to intake the remedies
        st.subheader('Instructions on how to intake the remedies:')
        for remedie in remedies:
            if 'Chandana' in remedie:
                st.subheader('Chandana')
                st.write('- Take Chandana (Sandalwood) powder and mix it with water to make a paste.')
                st.write('- Apply the paste on the forehead and temples for a cooling effect.')

            if 'Sheetali' in remedie:
                st.subheader("Sheetali")
                st.write('- Practice Sheetali pranayama (Cooling breath) to reduce body heat.')
                st.write('- Roll the sides of your tongue into a tube shape and inhale deeply through the tongue.')
                st.write('- Hold the breath for a few seconds and exhale through the nostrils.')

            if 'Yashtimadhu' in remedie:
                st.subheader('Yashtimadhus')
                st.write('- Take Yashtimadhu (Licorice) powder and mix it with warm water or milk.')
                st.write('- Consume the mixture before meals to soothe the digestive system.')

            if 'Hingu' in remedie:
                st.subheader('Hingu')
                st.write('- Dissolve Hingu (Asafoetida) powder in a glass of warm water.')
                st.write('- Drink the solution to alleviate symptoms of food poisoning.')

            if 'Nimba' in remedie:
                st.subheader('Nimba')
                st.write('- Prepare a decoction using Nimba (Neem) leaves.')
                st.write('- Drink the decoction to detoxify the body and treat vomiting caused by food poisoning.')

            if 'Guduchi' in remedie:
                st.subheader('Guduchi')
                st.write('- Take Guduchi (Tinospora Cordifolia) powder or extract.')
                st.write('- Mix it with honey or water and consume it to boost immunity and relieve vomiting symptoms.')

            if 'Patola' in remedie:
                st.subheader("Patola")
                st.write('- Include Patola (Pointed Gourd) in your diet.')
                st.write('- Cook it as a vegetable or consume its juice to improve digestion and reduce vomiting.')

            if 'Amalaki' in remedie:
                st.subheader('Amalaki')
                st.write('- Consume Amalaki (Indian Gooseberry) juice or powder.')
                st.write('- It helps in detoxifying the body and reducing the frequency of vomiting episodes.')

            if 'Brahmi' in remedie:
                st.subheader('Brahmi')
                st.write('- Take Brahmi (Bacopa Monnieri) powder or extract.')
                st.write('- Mix it with warm milk or water and consume it to reduce anxiety and relieve vomiting.')

            if 'Shankhapushpi' in remedie:
                st.subheader('Shankhapushpi')
                st.write('- Take Shankhapushpi (Convolvulus Pluricaulis) powder or extract.')
                st.write('- Mix it with honey or ghee and consume it to calm the mind and alleviate vomiting.')

            if 'Jatamansi' in remedie:
                st.subheader('Jatamansi')
                st.write('- Take Jatamansi (Nardostachys Jatamansi) powder or extract.')
                st.write('- Mix it with warm water or milk and consume it to reduce stress and prevent vomiting.')

            if 'Ginger' in remedie:
                st.subheader('Ginger')
                st.write('- Chew a small piece of fresh ginger or drink ginger tea.')
                st.write('- Ginger has anti-nausea properties and can help alleviate vomiting symptoms.')

            if 'Ajwain' in remedie:
                st.subheader('Ajwain')
                st.write('- Chew a teaspoon of Ajwain (Carom Seeds) to soothe the digestive system.')
                st.write('- It helps in reducing vomiting caused by motion sickness.')

            if 'Karpura' in remedie:
                st.subheader('Karpura')
                st.write('- Take a small amount of Karpura (Camphor) and dissolve it in warm water.')
                st.write('- Drink the solution to relieve migraine-related vomiting.')
