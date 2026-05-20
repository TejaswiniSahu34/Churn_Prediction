# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.set_page_config(page_title="Telecom Churn Dashboard", layout="wide")

st.title("📊 Telecom Customer Churn Analysis")

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("telecom_churn.csv")
    return df

df = load_data()

# Show Dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Dataset Information
st.subheader("Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", df.shape[0])

with col2:
    st.metric("Total Columns", df.shape[1])

with col3:
    churn_rate = (df['Churn'].value_counts(normalize=True)['Yes']) * 100
    st.metric("Churn Rate", f"{churn_rate:.2f}%")

# Churn Distribution
st.subheader("Churn Distribution")

fig, ax = plt.subplots()

df['Churn'].value_counts().plot(
    kind='bar',
    ax=ax
)

ax.set_xlabel("Churn")
ax.set_ylabel("Count")
ax.set_title("Customer Churn Count")

st.pyplot(fig)

# Gender Distribution
st.subheader("Gender Distribution")

fig2, ax2 = plt.subplots()

df['gender'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=ax2
)

ax2.set_ylabel("")

st.pyplot(fig2)

# Contract Type Analysis
st.subheader("Contract Type vs Churn")

contract_churn = pd.crosstab(df['Contract'], df['Churn'])

st.dataframe(contract_churn)

fig3, ax3 = plt.subplots()

contract_churn.plot(
    kind='bar',
    ax=ax3
)

ax3.set_title("Contract Type and Churn")
ax3.set_xlabel("Contract Type")
ax3.set_ylabel("Count")

st.pyplot(fig3)

# Monthly Charges Distribution
st.subheader("Monthly Charges Distribution")

fig4, ax4 = plt.subplots()

ax4.hist(df['MonthlyCharges'], bins=20)

ax4.set_xlabel("Monthly Charges")
ax4.set_ylabel("Frequency")
ax4.set_title("Monthly Charges Histogram")

st.pyplot(fig4)

# Sidebar Filters
st.sidebar.header("Filter Data")

selected_gender = st.sidebar.selectbox(
    "Select Gender",
    options=df['gender'].unique()
)

filtered_df = df[df['gender'] == selected_gender]

st.subheader(f"Filtered Data for {selected_gender}")

st.dataframe(filtered_df)

# Footer
st.success("Dashboard Created Successfully using Streamlit 🚀")