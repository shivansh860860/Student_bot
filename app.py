import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Companion", page_icon="🎓")

# Main title and subheader
st.title("🎓 Student Companion AI")
st.subheader("Created by Shivansh")

# Status and greeting
st.write("### Status: Online and Ready! ✅")
st.write("Hello! Ye mera pehla AI web app hai.")

# Button interaction
if st.button("Celebrate My First App!"):
    st.balloons()
    st.success("Congratulations! you are set to talk!")

# Sidebar info
st.sidebar.title("Project Info")
st.sidebar.info("Week 1: Successful Deployment")



