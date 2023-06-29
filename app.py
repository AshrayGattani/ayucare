
import streamlit as st

# Custom imports
from multipage import MultiPage
# import your pages here
from pages import home,general,pred,quiz,rem,fin,vomiting

# Create an instance of the app
app = MultiPage()



# Add all your applications (pages) here
app.add_page("Home Page", home.app)
app.add_page("General Remedies", rem.app)
app.add_page("Quiz", quiz.app)
app.add_page("Lifestyle Advices", general.app)
app.add_page("Disease Prediction", pred.app)
app.add_page('Charak Samhita',fin.app)
app.add_page('Disease Specific',vomiting.app)


# The main app
app.run()
