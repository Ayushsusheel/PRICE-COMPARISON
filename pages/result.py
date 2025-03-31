import streamlit as st
from price_scrapper_OR_BACKEND_CODE import get_amazon_details,get_flipkart_details  # Import price fetching function (Optional)

def show():
    st.title("💰 Price Comparison")
    
    st.markdown("<br />", unsafe_allow_html=True)
             
    if "mobile_name" in st.session_state:
        mobile_name = st.session_state["mobile_name"]
        st.write(f"Showing price comparison for : **{mobile_name}**")
        st.markdown(2 * "<br />", unsafe_allow_html=True)
        st.markdown("**************************************************")
        st.markdown("<br />", unsafe_allow_html=True)
        st.write(f"A M A Z O N  - D E T A I L  S :- ")
        st.markdown("<br />", unsafe_allow_html=True) 
        # Fetch prices (Replace this with real API/web scraping)
        price_data = get_amazon_details(mobile_name)  # Optional

        # for site, price in price_data.items():
        #     st.write(f"📌 {site}: **{price}**")

        for site_Thing, valueOfItem in price_data.items():
            st.write(f"📌 {site_Thing}: **{valueOfItem}**")   


    st.markdown("<br />", unsafe_allow_html=True) 
    st.markdown("**************************************************")
    st.markdown("<br />", unsafe_allow_html=True) 

    if "mobile_name" in st.session_state:
        mobile_name = st.session_state["mobile_name"]
        st.write(f"F L I P K A R T  - D E T A I L  S :- ")

        st.markdown("<br />", unsafe_allow_html=True)

        # Fetch prices (Replace this with real API/web scraping)
        price_data = get_flipkart_details(mobile_name)  # Optional

        # for site, price in price_data.items():
        #     st.write(f"📌 {site}: **{price}**")

        for site_Thing, valueOfItem in price_data.items():
            st.write(f"📌 {site_Thing}: **{valueOfItem}**")  

    st.markdown("<br />", unsafe_allow_html=True) 
    st.markdown("**************************************************")
    st.markdown("<br />", unsafe_allow_html=True) 

    if st.button("🔙 Back"):
        st.session_state["page"] = "home"
        st.rerun()





