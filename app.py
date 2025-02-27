import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the application
st.title('Exploratory Data Analysis with Streamlit')

#Display a simple text
st.write('This is a simple example of an EDA using Streamlit')


# Load the dataset
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})

## Display the dataset
st.write('Display the dataset')
st.write(df)


# Display a line chart
st.write('Display a line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

