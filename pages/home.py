import streamlit as st

def show():
    st.markdown(3 * "<br />", unsafe_allow_html=True)
    st.title("📱 Mobile Price Comparison!!")
    

    st.markdown(2 * "<br />", unsafe_allow_html=True)
    mobile_name = st.text_input("Enter Mobile Name")

    # my_index_Form = st.form(key='index_form')
    # productSelected = my_index_Form.selectbox("SELECT ANY PHONE TO COMPARE PRICE",["Redmi Note 14","Iphone 13","Realme 6 Pro","Realme GT-2","XYZ"])
    # searchButton = my_index_Form.form_submit_button("COMPARE PRICES")

#    
    st.markdown("<br />", unsafe_allow_html=True)
    
    
    if st.button("Submit"):
        if mobile_name:  # Ensure input is not empty
            st.session_state["mobile_name"] = mobile_name
            st.session_state["page"] = "result"

            # from price_scrapper_OR_BACKEND_CODE import get_amazon_details,get_flipkart_details
            # st.session_state["price_data"] = get_prices(mobile_name)
            # st.session_state["page"] = "price_scrapper_OR_BACKEND_CODE"
            
            
            
            
            st.rerun()  # Refresh to navigate
    


    # if(productSelected == "Redmi Note 14" or "Iphone 13" or "Realme 6 Pro" or "Realme GT-2" or "XYZ"):
    #          if searchButton:
    #              st.success("Hi, You Selected {} to compare price".format(productSelected))
    # else:
    #     st.error("Please select a valid product to compare price")