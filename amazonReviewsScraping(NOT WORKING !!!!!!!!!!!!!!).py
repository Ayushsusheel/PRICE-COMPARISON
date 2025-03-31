# # import requests
# # from bs4 import BeautifulSoup
# # import pandas as pd
# # from datetime import datetime


# # headers = ({
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
# #     "Accept-Language": "en-US,en;q=0.5"
# # })


# # amazon_RedmiNote14_Reviews_URL = "https://www.amazon.in/product-reviews/B0DPFV3T4V/ref=cm_cr_arp_d_paging_btm_next_6?ie=UTF8&reviewerType=all_reviews&pageNumber=1" 


# # len_page  = 10


# # #EXTRACT DATA AS HTML OBJ FROM AMAZON REVIEW PAGE

# # def getAmazonReviews_HTML(amazon_RedmiNote14_Reviews_URL,len_page):

# #     amazonSoups = []

# #     for page_no in range(1,len_page+1):

# #         # amazon_RedmiNote14_Reviews_URL = amazon_RedmiNote14_Reviews_URL[:-1] + str(page_no)

# #         # response = requests.get(amazon_RedmiNote14_Reviews_URL, headers=headers)
# #         # amazonSoup = BeautifulSoup(response.content, "html.parser")
# #         # amazonSoups.append(amazonSoup)
# #         params = {
# #             'ie': 'UTF8',
# #             'reviewerType': 'all_reviews',
# #             'pageNumber': page_no
# #         }

# #         #REQUEST MADE FOR EACH PAGE
# #         response = requests.get(amazon_RedmiNote14_Reviews_URL, headers=headers, params=params)
        
# #         #SAVE HTML OBJ BY USING BS4 and LXML PARSER
# #         amazonSoup = BeautifulSoup(response.content, "lxml")

# #         #APPEND EACH PAGE HTML OBJ TO LIST
# #         amazonSoups.append(amazonSoup)

# #     return amazonSoups


# # def getAmazonReviews(html_data):

# #     #creating empty list for storing reviews (CREATE EMPTY LIST TO HOLD ALL DATA)
# #     reviews = []

# #     #FINDING REVIEW CONTAINER
# #     boxes = html_data.select('div[data-hook="review"]')

# #     #LOOPING THROUGH EACH REVIEW (ITERATE ALL REVIEWS BOX)
# #     for box in boxes:

# #         #FINDING REVIEW TITLE
# #         title = box.select_one('a[data-hook="review-title"]').text.strip()

# #         #FINDING REVIEW RATING
# #         rating = box.select_one('i[data-hook="review-star-rating"]').text.strip()

# #         #FINDING REVIEW DATE
# #         date = box.select_one('span[data-hook="review-date"]').text.strip()

# #         #FINDING REVIEW BODY
# #         body = box.select_one('span[data-hook="review-body"]').text.strip()

# #         #APPENDING ALL DATA TO LIST
# #         reviews.append({
# #             'title': title,
# #             'rating': rating,
# #             'date': date,
# #             'body': body
# #         })


# # ================================================================================================================================================================================================================================================================


# # Import packages
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# from datetime import datetime

# # Header to set the requests as a browser requests
# headers = {
#     'authority': 'www.amazon.com',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

# }     #"Accept-Language": "en-US,en;q=0.5"




# # URL of The amazon Review page
# # reviews_url = 'https://www.amazon.com/Legendary-Whitetails-Journeyman-Jacket-Tarmac/product-reviews/B013KW38RQ/'
# amazon_RedmiNote14_Reviews_URL = "https://www.amazon.in/product-reviews/B0DPFV3T4V/ref=cm_cr_arp_d_paging_btm_next_6?ie=UTF8&reviewerType=all_reviews"   #&pageNumber=1"



# # Define Page No
# len_page = 10

# ### <font color="red">Functions</font>

# # Extra Data as Html object from amazon Review page
# def reviewsHtml(amazon_RedmiNote14_Reviews_URL, len_page):
    
#     # Empty List define to store all pages html data
#     soups = []
    
#     # Loop for gather all 3000 reviews from 300 pages via range
#     for page_no in range(1, len_page + 1):
        
#         # parameter set as page no to the requests body
#         params = {
#             'ie': 'UTF8',
#             'reviewerType': 'all_reviews',
#             # 'filterByStar': 'critical',
#             'pageNumber': page_no,
#         }
        
#         # Request make for each page
#         response = requests.get(amazon_RedmiNote14_Reviews_URL, headers=headers)
        
#         # Save Html object by using BeautifulSoup4 and lxml parser
#         soup = BeautifulSoup(response.text, 'lxml')
        
#         # Add single Html page data in master soups list
#         soups.append(soup)
        
#     return soups

# # Grab Reviews name, description, date, stars, title from HTML
# def getReviews(html_data):

#     # Create Empty list to Hold all data
#     data_dicts = []
    
#     # Select all Reviews BOX html using css selector
#     boxes = html_data.sele   #('div[data-hook="review"]')
    
#     # Iterate all Reviews BOX 
#     for box in boxes:
        
#         # Select Name using css selector and cleaning text using strip()
#         # If Value is empty define value with 'N/A' for all.
#         try:
#             name = box.select_one('[class="a-profile-name"]').text.strip()
#         except Exception as e:
#             name = 'N/A'

#         try:
#             stars = box.select_one('[data-hook="review-star-rating"]').text.strip().split(' out')[0]
#         except Exception as e:
#             stars = 'N/A'   

#         try:
#             title = box.select_one('[data-hook="review-title"]').text.strip()
#         except Exception as e:
#             title = 'N/A'

#         try:
#             # Convert date str to dd/mm/yyy format
#             datetime_str = box.select_one('[data-hook="review-date"]').text.strip().split(' on ')[-1]
#             date = datetime.strptime(datetime_str, '%B %d, %Y').strftime("%d/%m/%Y")
#         except Exception as e:
#             date = 'N/A'

#         try:
#             description = box.select_one('[data-hook="review-body"]').text.strip()
#         except Exception as e:
#             description = 'N/A'

#         # create Dictionary with al review data 
#         data_dict = {
#             'Name' : name,
#             'Stars' : stars,
#             'Title' : title,
#             'Date' : date,
#             'Description' : description
#         }

#         # Add Dictionary in master empty List
#         data_dicts.append(data_dict)
    
#     return data_dicts

# ### <font color="red">Data Process</font>

# # Grab all HTML
# html_datas = reviewsHtml(amazon_RedmiNote14_Reviews_URL, len_page)

# # Empty List to Hold all reviews data
# reviews = []

# # Iterate all Html page 
# for html_data in html_datas:
    
#     # Grab review data
#     review = getReviews(html_data)
    
#     # add review data in reviews empty list
#     reviews += review

# # Create a dataframe with reviews Data
# df_reviews = pd.DataFrame(reviews)

# print(df_reviews)

# # Save data
# df_reviews.to_csv('reviews.csv', index=False)