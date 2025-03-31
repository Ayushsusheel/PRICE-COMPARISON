import streamlit as st
from pages import home, result

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Navigation Logic
if st.session_state["page"] == "home":
    home.show()
elif st.session_state["page"] == "result":
    result.show()

