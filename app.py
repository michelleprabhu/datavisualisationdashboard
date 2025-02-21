import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Interactive Data Visualization Dashboard")

uploaded_file = st.file_uploader("Upload CSV Data", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())
    
    # Select column for visualization
    column = st.selectbox("Select Column to Visualize", df.columns)
    chart_type = st.radio("Choose Chart Type", ["Histogram", "Box Plot", "Scatter Plot"])
    
    if chart_type == "Histogram":
        fig = px.histogram(df, x=column, title=f"Distribution of {column}")
        st.plotly_chart(fig)
    elif chart_type == "Box Plot":
        fig = px.box(df, y=column, title=f"Box Plot of {column}")
        st.plotly_chart(fig)
    elif chart_type == "Scatter Plot":
        x_axis = st.selectbox("Select X-axis", df.columns)
        fig = px.scatter(df, x=x_axis, y=column, title=f"Scatter Plot of {column} vs {x_axis}")
        st.plotly_chart(fig)
    
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
