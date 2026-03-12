import streamlit as st

st.set_page_config(page_title="Student Companion", page_icon="🎓")

st.title("🎓 Student Companion AI")
st.subheader("Created by Shivansh")

st.write("### Status: Online and Ready! ✅")
st.write("Hello! Ye mera pehla AI web app hai.")

if st.button("Celebrate My First App!"):
st.balloons()
st.success("Congratulations! Shivansh, aapka code live ho gaya hai!")

st.sidebar.title("Project Info")
st.sidebar.info("Week 1: Successful Deployment")

