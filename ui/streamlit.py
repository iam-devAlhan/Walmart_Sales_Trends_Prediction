import streamlit as st
import pandas as pd
import numpy as np
import joblib
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Load dataset
file_path = "Walmart.csv"
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "yasserh/walmart-dataset",
    file_path,
)

# Preprocess date
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", errors="coerce")
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Week'] = df['Date'].dt.isocalendar().week

# Load trained model
model = joblib.load("../notebooks/walmart-sales-prediction-model.pkl")

# Get the feature names the model was trained on
model_features = model.feature_names_in_

st.title("How Unemployment Affects Weekly Sales")
st.write("Use the slider to explore how unemployment can impact weekly sales of stores. Walmart Sales Prediction Model is used for predictions. The Unemployment rate has low correlation with Weekly Sales, but it's interesting to see the model's behavior.")

# Slider for unemployment
unemployment = st.slider(
    "Unemployment Rate (%)",
    float(df['Unemployment'].min()),
    float(df['Unemployment'].max()),
    float(df['Unemployment'].mean())
)

# Prepare input for prediction
# Take the mean of all numeric columns in the dataset
input_features = df.drop(columns=["Weekly_Sales"]).mean().to_dict()
input_features['Unemployment'] = unemployment

# Keep only the columns the model expects
input_df = pd.DataFrame([{k: input_features[k] for k in model_features}])

# Predict
predicted_sales = model.predict(input_df)[0]
st.markdown(f"### Predicted Weekly Sales: {predicted_sales:,.0f}")

# Prepare chart data
unemp_range = np.linspace(df['Unemployment'].min(), df['Unemployment'].max(), 50)
sales_preds = []

for u in unemp_range:
    temp = input_features.copy()
    temp['Unemployment'] = u
    temp_df = pd.DataFrame([{k: temp[k] for k in model_features}])
    sales_preds.append(model.predict(temp_df)[0])

chart_data = pd.DataFrame({
    "Unemployment (%)": unemp_range,
    "Predicted Sales": sales_preds
})

# Line chart
st.line_chart(data=chart_data.set_index("Unemployment (%)"))
