import streamlit as st
def app():
        
    st.title('Ayurvedic Cures from Charaka Samhita')
    # Dictionary of health conditions and their sub-problems and corresponding cures
    health_conditions = {
        'Constipation': {
            'Aggravation of Vata Dosha': 'Triphala (A combination of three fruits - Haritaki, Bibhitaki, and Amalaki), Guggulu (Commiphora Mukul), Castor oil',
            'Lack of Exercise or Sedentary Lifestyle': 'Abhyanga (Ayurvedic oil massage), Udvartana (Dry powder massage), Surya Namaskar (Sun Salutation)',
            'Low Fiber Diet': 'Isabgol (Psyllium Husk), Triphala (A combination of three fruits - Haritaki, Bibhitaki, and Amalaki), Avipattikar Churna',
            'Dehydration': 'Ghee (Clarified Butter), Milk, Coconut water',
            'Poor Digestion': 'Ginger, Hing (Asafoetida), Pippali (Long Pepper)'
        },
        'Vomiting':{
            "Aggravation of Pitta Dosha": "Chandana (Sandalwood), Sheetali (Cooling), Yashtimadhu (Licorice)",
            "Food Poisoning": "Hingu (Asafoetida),Nimba (Neem),Guduchi (Tinospora Cordifolia)",
            "Gastrointestinal disorders": "Patola (Pointed Gourd),Amalaki (Indian Gooseberry),Yashtimadhu (Licorice)",
            "Emotional Disturbances": "Brahmi (Bacopa Monnieri),Shankhapushpi (Convolvulus Pluricaulis),Jatamansi (Nardostachys Jatamansi)",
            "Motion sickness": "Ginger, Ajwain (Carom Seeds), Shankhapushpi (Convolvulus Pluricaulis)",
            "Migraine": "Karpura (Camphor), Jatamansi (Nardostachys Jatamansi), Yashtimadhu (Licorice)"

        },
        'Diarrhea': {
            'Aggravation of Pitta Dosha': 'Kutaja (Holarrhena Antidysenterica), Bilva (Aegle Marmelos), Dhanyak (Coriander)',
            'Aggravation of Vata Dosha': 'Musta (Cyperus Rotundus), Bilva (Aegle Marmelos), Pomegranate juice',
            'Aggravation of Kapha Dosha': 'Haritaki (Terminalia Chebula), Bibhitaki (Terminalia Bellirica), Amalaki (Emblica Officinalis)',
            'Intestinal Infections': 'Kutaja (Holarrhena Antidysenterica), Musta (Cyperus Rotundus), Guduchi (Tinospora Cordifolia)',
            'Food Poisoning': 'Hingu (Asafoetida), Nimba (Neem), Guduchi (Tinospora Cordifolia)',
            'Stress and Anxiety': 'Brahmi (Bacopa Monnieri), Shankhapushpi (Convolvulus Pluricaulis), Jatamansi (Nardostachys Jatamansi)'
        },
        'Migraine': {
            'Aggravation of Pitta Dosha': 'Shatavari (Asparagus Racemosus), Brahmi (Bacopa Monnieri), Amalaki (Emblica Officinalis)',
            'Stress and Anxiety': 'Shankhapushpi (Convolvulus Pluricaulis), Jatamansi (Nardostachys Jatamansi), Ashwagandha (Withania Somnifera)',
            'Liver Dysfunction': 'Kutki (Picrorhiza Kurroa), Guduchi (Tinospora Cordifolia), Punarnava (Boerhavia Diffusa)',
            'Intestinal Disturbances': 'Hing (Asafoetida), Trikatu (A combination of ginger, black pepper, and long pepper), Guggulu (Commiphora Mukul)',
            'Environmental Factors': 'Tulsi (Ocimum Sanctum), Yashtimadhu (Glycyrrhiza Glabra), Guduchi (Tinospora Cordifolia)'
        },
        'Arthritis': {
            'Accumulation of Ama': 'Triphala (A combination of three fruits - Haritaki, Bibhitaki, and Amalaki), Guggulu (Commiphora Mukul), Kutki (Picrorhiza Kurroa)',
            'Imbalance of Vata Dosha': 'Maharasnadi Kwath, Ashwagandha (Withania Somnifera), Shallaki (Boswellia Serrata)',
            'Poor Digestion': 'Hing (Asafoetida), Trikatu (A combination of ginger, black pepper, and long pepper), Pippali (Long Pepper)',
            'Sedentary Lifestyle': 'Abhyanga (Ayurvedic oil massage), Udvartana (Dry powder massage), Surya Namaskar (Sun Salutation)',
            'Accumulation of Toxins': 'Guduchi (Tinospora Cordifolia), Neem (Azadirachta Indica), Manjistha (Rubia Cordifolia)'
        },
        'Insomnia': {
            'Imbalance of Vata Dosha': 'Brahmi (Bacopa Monnieri), Ashwagandha (Withania Somnifera), Shankhapushpi (Convolvulus Pluricaulis)',
            'Stress and Anxiety': 'Jatamansi (Nardostachys Jatamansi), Vacha (Acorus Calamus), Yashtimadhu (Glycyrrhiza Glabra)',
            'Poor Sleep Habits': 'Regular sleep routine, Avoiding caffeine and alcohol, Meditation',
            'Poor Digestion': 'Triphala (A combination of three fruits - Haritaki, Bibhitaki, and Amalaki), Hing (Asafoetida), Pippali (Long Pepper)',
            'Environmental Factors': 'Tulsi (Ocimum Sanctum), Chandan (Santalum Album), Lavender oil'
        },
        'Acidity': {
            'Imbalance of Pitta Dosha': 'Amla (Emblica Officinalis), Yashtimadhu (Glycyrrhiza Glabra), Shankhapushpi (Convolvulus Pluricaulis)',
            'Eating Spicy and Fried Foods': 'Cumin (Cuminum Cyminum), Coriander (Coriandrum Sativum), Fennel (Foeniculum Vulgare)',
            'Eating Large Meals or Overeating': 'Triphala (A combination of three fruits - Haritaki, Bibhitaki, and Amalaki), Guduchi (Tinospora Cordifolia), Pippali (Long Pepper)',
            'Eating Too Quickly': 'Chewing food properly, Eating mindfully, Avoiding talking while eating',
            'Stress and Anxiety': 'Brahmi (Bacopa Monnieri), Ashwagandha (Withania Somnifera), Shankhapushpi (Convolvulus Pluricaulis)'
        }
    }
    st.title("Health Condition ")
    health_condition = st.selectbox(
    'Select a health condition:',
    list(health_conditions.keys())
    )

    st.title("Sub problem")
    sub_problem = st.selectbox(
    'Select a sub-problem:',
    list(health_conditions[health_condition].keys())
    )

    cure = health_conditions[health_condition][sub_problem]
    st.title("Probable Cure:")
    # st.write(f"{sub_problem}: {cure}")
    st.write(f"<span style='font-size:20px'>{cure}</span>", unsafe_allow_html=True)

