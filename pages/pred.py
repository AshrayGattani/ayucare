import streamlit as st
import pickle
import pandas as pd
import random

def app():
  # def add_bg_from_url():
  #     st.markdown(
  #          f"""
  #          <style>
  #          .stApp {{
  #              background-image: url("https://images.unsplash.com/photo-1483137140003-ae073b395549?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxjb2xsZWN0aW9uLXBhZ2V8MTN8MzExOTU5NHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60");
  #              background-attachment: fixed;
  #              background-size: cover
  #          }}
  #          </style>
  #          """,
  #          unsafe_allow_html=True
  #      )

  # add_bg_from_url() 

  diseases_dict = pickle.load(open('pages/disease_dict.pkl','rb'))
  diseases = pd.DataFrame(diseases_dict)
  treatment = pickle.load(open('pages/treatment.pkl','rb'))


  cosine_sim = pickle.load(open('pages/similarity.pkl','rb'))
  indices = pd.Series(diseases['Symptoms'])

  def recommend(symptoms, cosine_sim = cosine_sim):
      recommended = []
      idx = indices[indices == symptoms].index[0]   # to get the index 
      score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = True)   # similarity scores in descending order
      top_5_indices = list(score_series.iloc[2:5].index)   # to get the indices of top 6 
      # [1:6] to exclude 0 
      
      for i in top_5_indices:   # to append the recommended
          recommended.append(list(diseases['Disease'])[i])
          
      return recommended



  def medi(dis):
    for index, row in treatment.iterrows():
      if row['Disease'] == dis:
        my_treat = ', '.join(row['Treatment'])
        return my_treat

  def rec(sym):
      for index, row in diseases.iterrows():
          if row['Symptoms'] == sym:
            my_dis = str(row['Disease'])
      return my_dis

  def how(dis):
    for index, row in treatment.iterrows():
      if row['Disease'] == dis:
        my_how = ', '.join(row['How to take'])
        return my_how


  st.title('Disease Prediction Using Symptoms')
  st.write("Select your symptoms")
  select_symptoms = st.selectbox('\n',diseases['Symptoms'].values)
  st.write("\n")
  st.write("\n")

  if st.button('Recommend'):
    dis = rec(select_symptoms)
    st.subheader('Disease Predicted : ')
    st.write(dis)
    st.subheader('Ayurveda Medication : ')
    medvv = medi(dis)
    st.write(medvv)
    st.subheader('How To Take : ')
    howj = how(dis)
    st.write(howj)
