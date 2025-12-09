import streamlit as st
import requests

st.set_page_config(
    page_title="Walmart Sales Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

st.title("Walmart Sales Prediction for better stock managing")
st.text("This demonstrates the walmart sales prediction based on the Walmart Sales Dataset, It predicts the sales according to given date and event such as Holiday and Non Holiday")
cols = st.columns([0.3, 0.7])
left_col = cols[0].container(
    border=True, height="stretch", vertical_alignment="center"
)
right_col = cols[1].container(
    border=True, height="content", vertical_alignment="center"
)
with left_col:
    date_input = st.date_input(label="Enter Date to continue")
    is_holiday = st.selectbox(label="Select Holiday", options=["Non Holiday", "Holiday"])
    predict = st.button("Predict")

    # Added mock data , later adding it prediction
    if predict:
        st.metric("Predicted Sales", "70%")

with right_col:
    st.bar_chart(x_label="Sales", height="stretch")