# import streamlit as st


# st.title("_PRICE COMPARISON_ :blue[AMZAON, FLIPKART] ")

# st.page_link("http://www.google.com", label="BUY FROM GOOGLE", icon="🌎")
# st.page_link("http://www.amazon.com", label="BUY FROM Amazon", icon="🛒")



# import streamlit as st

# # Initialize session state
# if "page" not in st.session_state:
#     st.session_state["page"] = "home"

# def home_page():
#     st.title("Mobile Price Comparison")
#     mobile_name = st.text_input("Enter Mobile Name")

#     if st.button("Submit"):
#         if mobile_name:  # Ensure input is not empty
#             st.session_state["mobile_name"] = mobile_name
#             st.session_state["page"] = "result"
#             st.rerun()  # Rerun the script to refresh the page

# def result_page():
#     st.title("Price Comparison Results")
    
#     if "mobile_name" in st.session_state:
#         mobile_name = st.session_state["mobile_name"]
#         st.write(f"Showing price comparison for: **{mobile_name}**")

#         # Dummy price data (Replace with actual API calls)
#         price_data = {
#             "Amazon": "$500",
#             "Flipkart": "$480",
#             "eBay": "$510"
#         }

#         for site, price in price_data.items():
#             st.write(f"📌 {site}: **{price}**")

#     if st.button("Back"):
#         st.session_state["page"] = "home"
#         st.rerun()  # Rerun to go back

# # Page Router
# if st.session_state["page"] == "home":
#     home_page()
# elif st.session_state["page"] == "result":
#     result_page()
