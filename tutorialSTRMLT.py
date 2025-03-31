# --------------------------------------------------------------


# import streamlit as st

# "# Header 1"
# st.title('Hello World!')


# "## Header 2"
# st.write('This is a simple web app created using Streamlit')


# "### Header 3"
# "This is a simple web app created using Streamlit"

# "### Header 3"
# st.caption("This is a simple web app created using Streamlit")



# st.caption("[ BUTTON ]")

# col1,col2,col3 = st.columns(3)
# with col1:
#     st.button('Button 1')
#     st.header("AMAZON")
#     st.image("https://www.amazon.in/images/I/71A9Vo1BatL._AC_SL1500_.jpg",width=200)

# with col2:
#     st.button('Button 2')
#     st.header("FLIPKART")
#     # st.image("/resources/flipkartLogo.png",width=200)




# st.html(
#     "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
# )


# st.title("This is a title")
# st.title("_PRICE COMPARISON_ :blue[AMZAON, FLIPKART] :sunglasses:")




# st.header("_Streamlit_ is :blue[cool] :sunglasses:")
# st.header("This is a header with a divider", divider="gray")
# st.header("These headers have rotating dividers", divider=True)
# st.header("One", divider=True)
# st.header("Two", divider=True)
# st.header("Three", divider=True)
# st.header("Four", divider=True)






# import random
# import pandas as pd
# import streamlit as st

# df = pd.DataFrame(
#     {
#         "name": ["Roadmap", "Extras", "Issues"],
#         "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
#         "stars": [random.randint(0, 1000) for _ in range(3)],
#         "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
#     }
# )
# st.dataframe(
#     df,
#     column_config={
#         "name": "App named",
#         "stars": st.column_config.NumberColumn(
#             "Github Stars",
#             help="Number of stars on GitHub",
#             format="%d ⭐",
#         ),
#         "url": st.column_config.LinkColumn("App URL"),
#         "views_history": st.column_config.LineChartColumn(
#             "Views (past 30 days)", y_min=0, y_max=5000
#         ),
#     },
#     hide_index=True,
# )




# import streamlit as st

# st.link_button("Go to gallery", "https://streamlit.io/gallery")




# import streamlit as st

# # st.page_link("F:/1.0 T H A P A R/SUBJECTS/sem2/6.0 Human Centered/LAB/project/WEB_SCRAPING_FAKE_REVIEW/app.py", label="Home", icon="🏠")
# # st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
# # st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
# st.page_link("http://www.google.com", label="BUY FROM GOOGLE", icon="🌎")
# st.page_link("http://www.amazon.com", label="BUY FROM Amazon", icon="🛒")




# import streamlit as st

# title = st.text_input("Movie title", "Life of Brian")
# st.write("The current movie title is", title)


# import time
# import streamlit as st

# with st.status("Downloading data...", expanded=True) as status:
#     st.write("Searching for data...")
#     time.sleep(2)
#     st.write("Found URL.")
#     time.sleep(1)
#     st.write("Downloading data...")
#     time.sleep(1)
#     status.update(
#         label="Download complete!", state="complete", expanded=False
#     )

# st.button("Rerun")


# # import streamlit as st
# # import time

# # with st.spinner("Wait for it...", show_time=True):
# #     time.sleep(5)
# # st.success("Done!")
# # st.button("Rerun")


# import streamlit as st

# st.success('This is a success message!', icon="✅")


# import streamlit as st

# st.error('This is an error', icon="🚨")



# import streamlit as st

# def page2():
#     st.title("Second page")

# pg = st.navigation([
#     st.Page("app.py", title="First page", icon="🔥"),
#     st.Page(page2, title="Second page", icon=":material/favorite:"),
# ])
# pg.run()

# ------------------------------------------------------------------------
import streamlit as st

# "# Header 1"
st.title('Welcome to price comparison webApap!')

#HEADER/SUBHEADER , TEXT ,MARKDOWN
# st.markdown("HELLO")
# st.markdown("### hello")

st.header("AMAZON")
st.subheader("Redmi Note 14 ")
st.text("Price: ₹ 15,999")
st.text("Rating: 4.5")


#ERROR/SUCCESS
st.success("Successfully fetched the details")
st.error("Error while fetching the details")
st.info("Information")
st.warning("Warning")





st.header("FLIPKART")
st.subheader("Redmi Note 14 ")




#EXCEPTION
st.exception("This is an exception") 


#WRITE
st.write("This is a write statement")

#IMAGES
from PIL import Image
image = Image.open("resources/amazonLogo.png")
st.image(image, caption='Amazon Logo',use_column_width=True) 







# ----------------------------------------------------------------------

import streamlit as st

#IMAGES
from PIL import Image
image = Image.open("resources/amazonLogo.png")
st.image(image, caption='Amazon Logo',width=300) #,use_column_width=True 



image = Image.open("resources/flipkartLogo.png")
st.image(image, caption='Flipkart Logo',width=300) #,use_column_width=True 


# #ADD VIDEO
# video_file = open('resources/Amazon.mp4', 'rb')
# video_bytes = video_file.read()
# st.video(video_bytes)

#ADD AUDIO
# audio_file = open('resources/Amazon.mp3', 'rb').read() 
# st.audio(audio_file) #,format='audio/mp3'


#CHECKBOX (I WANT TO SEE NAME, PRICE, RATING, REVIEWS ETC)
if st.checkbox("SHOW / HIDE DETAILS"):
    st.text("Showing Details")


#RADIO BUTTONS
## st.write("Select the Website you want to compare the prices of the product")
## option = st.radio(
##     'Select the Website',
##     ('Amazon', 'Flipkart')
## )

status = st.radio("Waht is your status",("Active","Inactive"))



#LINK with some function
if status=="Active":
    st.success("You are Active")
else:
    st.error("You are Inactive")    



#SELECT BOX
occupation = st.selectbox("Your Occupation",["Programmer","Data Scientist","Doctor","Engineer","Teacher"])
st.write("You selected this option",occupation)


#MULTISELECT
location = st.multiselect("Where do you work?",("India","USA","UK","Australia","Germany"))


#SLIDER
level = st.slider("What is your level",1,5)

#BUTTON

# 1) 
# st.button("Simple Button")

# 2)
if st.button("ABOUT / SUBMIT BUTTON"): 
    # st.success("Submitted")
    st.text("Submitted")
    st.write("You selected this option",occupation)


#TEXT INPUT (key=1 means if i'm taking multiple inputs then i have to define multiple keys like 1,2,3,4,5,6  )
name = st.text_input("Enter your name","Type Here...")
if st.button("Submit",key ="1"):
    result = name.title()
    st.success(result)


#TEXT AREA
message = st.text_area("Enter your comments","Type Here...")
if st.button("Submit",key ="2"):
    result = message.title()
    st.success(result)


#DATE INPUT
import datetime
today = st.date_input("Today is",datetime.datetime.now())

#TIME INPUT
the_time = st.time_input("The time is",datetime.time())


#LOADING BAR
import time
with st.spinner("LOADING DETAILS..."):
    time.sleep(5)
    st.success("Finished!")

#SIDEBAR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tutorial")
