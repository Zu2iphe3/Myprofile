# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#import streamlit as st 
#st.title("Streamlit is amazing!")
#st.title("Never use spaces in folder names")
#st.write("Ndiyagowa Yooh")


#st.write("This is my first web page..")

#number = st.slider("Pick a {number}", 1, 100)
#st.write("Pick a {number}")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown('<h1 style="color: navy;">Academic Profile</h1>', unsafe_allow_html=True)

#The sidebar organizes the app by allowing users to switch between different sections (like "Researcher Overview," "Publications," etc.) through a radio button.
st.sidebar.header("Navigation")
selected_section = st.sidebar.radio("Go to", ["Researcher Overview","Publications", "Contact Information"])

st.markdown("---")
# Title of the app
#st.title("Academic Profile")

# Collect basic information
name = "Zusiphe Mzazela"
field = "MSc Med Bioinformatics"
focus = "Machine Learning, Epigenetics, and Cancer Informatics"
institution = "University of Cape Town"

if selected_section == "Researcher Overview":
    st.header("Researcher Overview")
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Areas of Expertise:** {focus}")
    st.write(f"**Institution:** {institution}")

# Display basic profile information
#st.header("Researcher Overview")
#st.write(f"**Name:** {name}")
#st.write(f"**Field of Research:** {field}")
#st.write(f"**Specialisation:** {focus}")
#st.write(f"**Institution:** {institution}")

# Add a section for publications
#st.header("Publications")
#uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

# Add a section for publications
st.markdown('<h3 style="color: teal;">Publications 📄</h3>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
 
if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Mock Feature Importance Plot for BRCA Subtype Classification
if selected_section == "Publications":
    st.header("Key Feature Contributions for BRCA Subtype Prediction")

    # Example feature names and importance scores
    features = ["Gene_1", "Gene_2", "Gene_3", "Gene_4", "Gene_5"]
    importances = [0.25, 0.20, 0.15, 0.30, 0.10]

    # Create a bar plot for feature importances
    fig, ax = plt.subplots()
    ax.barh(features, importances, color='teal')
    ax.set_title("Top Feature Importances for Subtype Prediction")
    ax.set_xlabel("Importance Score")
    ax.set_ylabel("Features")
    st.pyplot(fig)
    
# Add a contact section
st.header("Contact Information")
email = "mzzzus001@myuct.ac.za"
#st.write(f"You can reach {name} at {email}.")


# Add a unified contact and collaboration section
st.markdown('<h2 style="color: darkgreen;">📬 Connect & Collaborate</h2>', unsafe_allow_html=True)
st.write(
    "Thank you for visiting my academic profile! I am always open to research collaborations, discussions, and insights in **bioinformatics and machine learning in healthcare.** Let's explore groundbreaking ideas together!"
)
st.write(f"📧 **Email:** {email}")  # Correct use of the f-string with the placeholder

# Contact form for user engagement
st.write("📤 Leave a message below if you'd like to connect or share research ideas.")
with st.form(key="contact_form"):
    user_message = st.text_area("Your Message for Zusiphe")
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        st.success("Thank you for your message! I'll get back to you shortly.")
