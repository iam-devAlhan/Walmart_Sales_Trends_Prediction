import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Walmart Sales Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

st.title("Walmart Sales Prediction for Better Stock Management")
st.text("This demonstrates the Walmart sales prediction based on the dataset. Predicts sales according to date and holiday event.")

# Create two columns: left for input, right for chart
left_col, right_col = st.columns([0.3, 0.7])

with left_col:
    date_input = st.date_input("Enter Date to continue")
    is_holiday = st.selectbox("Select Holiday", ["Non Holiday", "Holiday"])
    predict = st.button("Predict")

    if predict:
        # For now mock prediction
        predicted_sales = 1640000  # Replace later with model.predict(...)
        st.metric("Predicted Sales", f"${predicted_sales:,.2f}")

with right_col:
    # Example mock data for chart
    df_chart = pd.DataFrame({
        "Sales": np.random.randint(1400000, 1700000, size=10),
        "Week": [f"Week {i+1}" for i in range(10)]
    })
    st.bar_chart(data=df_chart.set_index("Week"), color="#0FD83A")
