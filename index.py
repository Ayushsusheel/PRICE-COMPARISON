import streamlit as st


#SEARCH BAR
# st.title("_PRICE COMPARISON_ :blue[AMZAON, FLIPKART] ") #:sunglasses:

# search = st.text_input("Search for a product")
# searchButton = st.button("Search")


# productSelected = st.selectbox("SELECT ANY PHONE TO COMPARE PRICE",["Redmi Note 14","Iphone 13","Realme 6 Pro","Realme GT-2","XYZ"])
# # searchButton = st.button("COMPARE PRICE")
# st.link_button("COMPARE PRICE", "py_files/comparePrices.py")
# st.write("You selected this option",productSelected)




# import time
# with st.spinner("LOADING DETAILS..."):
#     time.sleep(5)
#     st.success("Finished!")

# st.header(productSelected)



# st.page_link("F:/1.0 T H A P A R/SUBJECTS/sem2/6.0 Human Centered/LAB/project/WEB_SCRAPING_FAKE_REVIEW/app.py", label="Home", icon="🏠")
# st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
# st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)



# --------------------------------------------------------------


st.title("_PRICE COMPATRISON_ :blue[AMZAON, FLIPKART] ") #:sunglasses:

# with st.form(key='index_form'):
my_index_Form = st.form(key='index_form')
productSelected = my_index_Form.selectbox("SELECT ANY PHONE TO COMPARE PRICE",["Redmi Note 14","Iphone 13","Realme 6 Pro","Realme GT-2","XYZ"])
searchButton = my_index_Form.form_submit_button("COMPARE PRICE")

if(productSelected == "Redmi Note 14" or "Iphone 13" or "Realme 6 Pro" or "Realme GT-2" or "XYZ"):
    if searchButton:
        st.success("Hi, You Selected {} to compare price".format(productSelected))
else:
    st.error("Please select a valid product to compare price")

# col1, col2 = st.columns(2)

# with col1:
#     with st.form(key='form1'):
#         productSelected = st.selectbox("SELECT OPTIONS",["PRICE","RATING","BUY URL"])
#         searchButton = st.form_submit_button("COMPARE PRICE")
#         st.write("You selected this option",productSelected)



# with col1:
#     with st.form(key='form2'):
#         productSelected = st.selectbox("SELECT OPTIONS",["PRICE","RATING","BUY URL"])
#         searchButton = st.form_submit_button("COMPARE PRICE")
#         st.write("You selected this option",productSelected)
