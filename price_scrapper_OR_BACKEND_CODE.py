import streamlit as st
from backendCode import amazon_title, amazon_price, amazon_rating, get_amazon_reviews,amazonUrl_RedmiNote14, flipkartUrl_RedmiNote14, flipkart_title, flipkart_price, flipkart_rating




def get_amazon_details(mobile_name):
        # Dummy data (Replace this with web scraping or API calls)
 
    mobile_name = mobile_name.replace(" ", "").strip(" ").lower()

    if mobile_name == "redminote14":
        return {
         # "Amazon": "$500",
         # "Flipkart": "$480",
         # "eBay": "$510"

            "Amazon Title": amazon_title,
           "Amazon Price": amazon_price,
         "Amazon Rating": amazon_rating,
         # "Amazon Review": get_amazon_reviews(),
         "BUY URL" : amazonUrl_RedmiNote14
        }
    else:
        return {"SORRY AS OF NOW I CAN DISPLAY DATA FOR :---->  " : "REDMI NOTE 14"}



def get_flipkart_details(mobile_name):
            
    mobile_name = mobile_name.replace(" ", "").strip(" ").lower()

    if mobile_name == "redminote14":
            return {
            # "Amazon": "$500",
            # "Flipkart": "$480",
            # "eBay": "$510"

            "Flipkart Title": flipkart_title,
            "Flipkart Price": flipkart_price,
            "Flipkart Rating": flipkart_rating,
            # "Amazon Review": get_amazon_reviews(),
            "BUY URL" : flipkartUrl_RedmiNote14
      }
    else:
        return {"SORRY AS OF NOW I CAN DISPLAY DATA FOR :---->  " : "REDMI NOTE 14"}


