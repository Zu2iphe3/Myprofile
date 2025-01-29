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

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
    
# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Zusiphe Mzazela"
field = "MSc Med Bioinformatics"
focus = "Machine Learning"
institution = "University of Cape Town"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Specialisation:** {focus}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
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

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "mzzzus001@myuct.ac.za"
st.write(f"You can reach {name} at {email}.")