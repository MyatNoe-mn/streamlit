

import streamlit as st

#number = st.number_input("Insert a number")
#st.write("The current number is ", number)
#st.write(7*number)

#import datetime

#d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
#st.write("Your birthday is:", d)

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Phone", "Whatsapp" , "Wechat"))

st.write("You selected:", option)