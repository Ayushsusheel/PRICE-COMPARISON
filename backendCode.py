# from pyscript import document as doc
# print("Hello World in console from app.py file")  

# outputDiv = doc.querySelector('#textarea')
# outputDiv.innerText = 'Hello World from app. py file'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                      [AMAZON PROJECT STARTS HERE]

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import requests
import pandas as pd

amazonUrl_RedmiNote14 = "https://www.amazon.in/Redmi-Note-14-5G-Dimensity/dp/B0DPFV3T4V?th=1"

# amazonReviewsUrl = "https://www.amazon.in/product-reviews/B0DPFV3T4V/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

headers = ({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
})


#--------------------------------CREATING HTTP REQUEST TO GET THE DATA FROM THE AMAZON WEBSITE
webpage = requests.get(amazonUrl_RedmiNote14, headers=headers)
print("\n----------------------------------------------------------[ AMAZON STATUS CODE ]---------------------------------------------------")
print(webpage.status_code)
# print(webpage.content)
print("------------------------------------------------------------------------------------------------------------------------------\n")



#--------------------------------PARSING THE WEBPAGE USING BEAUTIFULSOUP
amazonSoup = BeautifulSoup(webpage.content, 'html.parser')
# print(amazonSoup.prettify())

#----------------------------------------------------------[ FETCHING TITLE OF THE PRODUCT ]----------------------------------------------------------
# amazon_title = amazonSoup.find('div',attrs={'id':'titleSection'}).find('h1',attrs={'id':'title'}).find('span',attrs={'id':'productTitle'}).text()

# amazon_title = amazonSoup.find("span",class_='a-size-large product-title-word-break').get_text().strip()

amazon_title = amazonSoup.find('span',attrs={'id':'productTitle'}).get_text().strip()

print("\n----------------------------------------------------------[ AMAZON  NAME ]----------------------------------------------------------")
print(amazon_title)
print("------------------------------------------------------------------------------------------------------------------------------")


#----------------------------------------------------------[ FETCHING PRICE OF THE PRODUCT ]----------------------------------------------------------
amazon_price = amazonSoup.find("span",attrs={'class':'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).get_text().strip()
print("\n----------------------------------------------------------[ AMAZON  PRICE ]---------------------------------------------------------")
print(amazon_price)
print("------------------------------------------------------------------------------------------------------------------------------")



#----------------------------------------------------------[ FETCHING RATING OF THE PRODUCT ]----------------------------------------------------------
amazon_rating = amazonSoup.find("span",attrs={'class':'a-icon-alt'}).get_text().strip()
print("\n----------------------------------------------------------[ AMAZON  RATING ]--------------------------------------------------------")
print(amazon_rating)
print("------------------------------------------------------------------------------------------------------------------------------")



# def get_title(soup):
#     try:
#         title = soup.find("span",attrs={'id':'productTitle'}).get_text().strip()
#     except:
#         title = ''
#     return title


# TITLE PRINT KAR RA HAI  (Redmi Note 14 5G (Mystique White, 8GB RAM 128GB Storage) | Global Debut MTK Dimensity 7025 Ultra | 2100 nits Segment Brightest 120Hz AMOLED | 50MP Sony LYT 600 OIS+EIS Triple Camera : Amazon.in)
# print(amazonSoup.title.text)

                              #"div"   
reviews = amazonSoup.find_all("li",{"data-hook":"review"}) #FIND ALL NOW WILL BASICALLY GIVE US A LIST OF ALL THE REVIEWS


# print(reviews) #------------------>(IT WILL PRINT ALL THE DIV i.e Whole Conatiner which has all the tags span,img,i,REVIEWS etc......)


# BOX = amazonSoup.find_all("div",class_="a-section celwidget")
# print(len(BOX))
# personName = []
# title = []
# rating = []

# name = amazonSoup.find("div",attrs={'class':'a-profile-content'}).find("span",attrs={'class':'a-profile-name'}).text.strip()
# print(name)

# for i in BOX:

    # personName.append(i.find("div",class_="a-profile-content").text.strip())
    # title.append(i.find("h5"))
    #  rating.append(i.find("i",{"data-hook":"review-star-rating"}).text.strip())
    # rating.append(i.find("i",class_="a-icon").text.strip())

# print(title)
# print(personName)
# print(rating)


# def get_reviews(soup):
#     try:
#         reviews = soup.find_all("li",{"data-hook":"review"})
#     except:
#         reviews = ''
#     return reviews


def get_amazon_reviews():
        i = 1
        for item in reviews:

         #     print(item.text.strip())
    
         # title  = item.find("a",{"data-hook":"review-title"}).text.strip()
         # rating = item.find("i",{"data-hook":"review-star-rating"}).text.strip()
         # review = item.find("span",{"data-hook":"review-body"}).text.strip()

             review = {
                        'productName' : amazonSoup.title.text.replace("Amazon.in", "").strip(),
                        'title' : item.find("a",{"data-hook":"review-title"}).text.strip(),
                        'rating' : item.find("i",{"data-hook":"review-star-rating"}).text.strip(),
                         'review' : item.find("span",{"data-hook":"review-body"}).text.strip()
    

    # title = item.find("a",{"data-hook":"review-title"}).text.strip()
# allReviews = amazonSoup.find_all("div",class_="a-section celwidget")
#print(allReviews) #------------------->(IT WILL PRINT ALL THE TAGS OF THE PAGE)

# # YE MERA 1ST CONTAINER H (1ST COMMENT WALA PURA BOX H YE)
# box = amazonSoup.find_all("div",class_="a-section celwidget")[0]
# print(box)

# title = box.find("a").text
# print(title)

    # rating = item.find("i",{"data-hook":"review-star-rating"}).text.strip()
    # print(rating)  #------------------->(IT WILL PRINT ALL THE RATINGS OF THE REVIEWS)


    # reviewBody = item.find("span",{"data-hook":"review-body"}).text  #.strip() is used to remove the extra spaces
    # print(reviewBody)  #------------------->(IT WILL PRINT ALL THE REVIEWS)
    
                            }

        print("\n----------------------------------------------------------[ AMAZON  REVIEWS", i ," ]-----------------------------------------------------------------------------------------")
        print(review)
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        i+=1
        return review


    
get_amazon_reviews()





# https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY/ref=sr_1_1_sspa?crid=2IO9IL4VIM6HE&dib=eyJ2IjoiMSJ9.8-aKrERwPzdGyJWfWOa56I4wwdlI59jT8Bz9mNMoRuLX6-Z_YfKh0arrEePiEGDN1qYP0OgioucZNGzMdIdTkAO3S6ih0DqmQrTjoc6_TvIga7GvzvVQFkSD6ZefJzVffyHHc5XN0IitRwwCbSMjV0M4-AtkNAF-DeMKMEYcEAWKWV3kqHFMNTUsoW6rVKcyhfoTUWhserYRB6gaVhhi7zc2pwBjntvEv4klEUehfpOqoyg2fQH57F2hJ10Yy8yk9oIa4YEi7c0bPcjKri_bdOPwdYyWRxBLDG4K_D_f4Wg.nzP-C_gtYbPpWlBcyxqbzDM1C33fR7-VobHKIULfY64&dib_tag=se&keywords=iphone%2B15%2Bblack%2B128gb&qid=1742884038&s=electronics&sprefix=iphone%2B15%2Bblack128gb%2Celectronics%2C261&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1









# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                               [FLIPKART PROJECT STARTS HERE]

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
import pandas as pd


flipkartUrl_RedmiNote14 = "https://www.flipkart.com/redmi-note-14-5g-mystique-white-128-gb/p/itm721548515fde2?pid=MOBH78KTV8NBYHTH&lid=LSTMOBH78KTV8NBYHTHKYZXD7&marketplace=FLIPKART"

# amazonReviewsUrl = "https://www.amazon.in/product-reviews/B0DPFV3T4V/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

headers = ({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
})


#--------------------------------CREATING HTTP REQUEST TO GET THE DATA FROM THE AMAZON WEBSITE
webpage = requests.get(flipkartUrl_RedmiNote14, headers=headers)
print("\n\n\n\n\n\n----------------------------------------------------------[ FLIPKART STATUS CODE ]---------------------------------------------------")
print(webpage.status_code)
# print(webpage.content)
print("------------------------------------------------------------------------------------------------------------------------------\n")



#--------------------------------PARSING THE WEBPAGE USING BEAUTIFULSOUP
flipkartSoup = BeautifulSoup(webpage.content, 'html.parser')
# print(flipkartSoup.prettify())

#----------------------------------------------------------[ FETCHING TITLE OF THE PRODUCT ]----------------------------------------------------------
flipkart_title = flipkartSoup.find("h1",attrs={'class':'_6EBuvT'}).get_text().strip()

print("\n----------------------------------------------------------[  FLIPKART   NAME ]----------------------------------------------------------")
print(flipkart_title)
print("------------------------------------------------------------------------------------------------------------------------------")


# #----------------------------------------------------------[ FETCHING PRICE OF THE PRODUCT ]----------------------------------------------------------
flipkart_price = flipkartSoup.find("div",attrs={'class':'Nx9bqj'}).get_text().strip() #'class':'Nx9bqj'
print("\n----------------------------------------------------------[  FLIPKART   PRICE ]---------------------------------------------------------")
print(flipkart_price)
print("------------------------------------------------------------------------------------------------------------------------------")



#----------------------------------------------------------[ FETCHING RATING OF THE PRODUCT ]----------------------------------------------------------
flipkart_rating = flipkartSoup.find("div",attrs={'class':'XQDdHH'}).get_text().strip()
print("\n----------------------------------------------------------[  FLIPKART   RATING ]--------------------------------------------------------")
print(flipkart_rating)
print("------------------------------------------------------------------------------------------------------------------------------")



# def get_title(soup):
#     try:
#         title = soup.find("span",attrs={'id':'productTitle'}).get_text().strip()
#     except:
#         title = ''
#     return title


# TITLE PRINT KAR RA HAI  (Redmi Note 14 5G (Mystique White, 8GB RAM 128GB Storage) | Global Debut MTK Dimensity 7025 Ultra | 2100 nits Segment Brightest 120Hz AMOLED | 50MP Sony LYT 600 OIS+EIS Triple Camera : Amazon.in)
# print(amazonSoup.title.text)

                              #"div"   
# reviews = amazonSoup.find_all("li",{"data-hook":"review"}) #FIND ALL NOW WILL BASICALLY GIVE US A LIST OF ALL THE REVIEWS
# print(reviews) #------------------>(IT WILL PRINT ALL THE DIV i.e Whole Conatiner which has all the tags span,img,i,REVIEWS etc......)


# BOX = amazonSoup.find_all("div",class_="a-section celwidget")
# print(len(BOX))
# personName = []
# title = []
# rating = []

# name = amazonSoup.find("div",attrs={'class':'a-profile-content'}).find("span",attrs={'class':'a-profile-name'}).text.strip()
# print(name)

# for i in BOX:

    # personName.append(i.find("div",class_="a-profile-content").text.strip())
    # title.append(i.find("h5"))
    #  rating.append(i.find("i",{"data-hook":"review-star-rating"}).text.strip())
    # rating.append(i.find("i",class_="a-icon").text.strip())

# print(title)
# print(personName)
# print(rating)
i = 1

# def get_reviews(soup):
#     try:
#         reviews = soup.find_all("li",{"data-hook":"review"})
#     except:
#         reviews = ''
#     return reviews


# def get_amazon_reviews():
#         for item in reviews:

#          #     print(item.text.strip())
    
#          # title  = item.find("a",{"data-hook":"review-title"}).text.strip()
#          # rating = item.find("i",{"data-hook":"review-star-rating"}).text.strip()
#          # review = item.find("span",{"data-hook":"review-body"}).text.strip()

#              review = {
#                         'productName' : amazonSoup.title.text.replace("Amazon.in", "").strip(),
#                         'title' : item.find("a",{"data-hook":"review-title"}).text.strip(),
#                         'rating' : item.find("i",{"data-hook":"review-star-rating"}).text.strip(),
#                          'review' : item.find("span",{"data-hook":"review-body"}).text.strip()
    

    # title = item.find("a",{"data-hook":"review-title"}).text.strip()
# allReviews = amazonSoup.find_all("div",class_="a-section celwidget")
#print(allReviews) #------------------->(IT WILL PRINT ALL THE TAGS OF THE PAGE)

# # YE MERA 1ST CONTAINER H (1ST COMMENT WALA PURA BOX H YE)
# box = amazonSoup.find_all("div",class_="a-section celwidget")[0]
# print(box)

# title = box.find("a").text
# print(title)

    # rating = item.find("i",{"data-hook":"review-star-rating"}).text.strip()
    # print(rating)  #------------------->(IT WILL PRINT ALL THE RATINGS OF THE REVIEWS)


    # reviewBody = item.find("span",{"data-hook":"review-body"}).text  #.strip() is used to remove the extra spaces
    # print(reviewBody)  #------------------->(IT WILL PRINT ALL THE REVIEWS)
    
        #                     }

        # print("\n----------------------------------------------------------[  FLIPKART   REVIEWS", i ," ]-----------------------------------------------------------------------------------------")
        # print(review)
        # print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        # i+=1
        # return review
    
