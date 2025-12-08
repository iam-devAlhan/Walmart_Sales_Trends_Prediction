import streamlit as st
import requests

st.title("Walmart Sales Prediction for better stock managing")
st.text("This demonstrates the walmart sales prediction based on the Walmart Sales Dataset, It predicts the sales according to given date and event such as Holiday and Non Holiday")


date_input = st.date_input(label="Enter Date to continue")
is_holiday = st.selectbox(label="Select Holiday", options=["Holiday", "Non Holiday"])
predict = st.button("Predict")

# Added mock data , later adding it prediction
if predict:
    st.metric("Predicted Sales", "70%")
