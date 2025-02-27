import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the application
st.title('Exploratory Data Analysis with Streamlit')

name = st.text_input('Enter your name')

if name:
    st.write('Hello', name)
    
age = st.number_input('Enter your age')
     
age = st.slider('Enter your age', 0, 100,25)
if age:
    st.write('Your age is',
                age)

options = st.selectbox('What is your favorite color?',
                        ['Red', 'Green', 
                        'Blue'])
st.write('You selected:', options)

options = st.multiselect('What are your favorite colors?',
                        ['Red', 'Green', 
                        'Blue'])

st.write('You selected:', options)

data = pd.DataFrame({
    'Name': ['Tom', 'Nick', 'John', 'Tom', 'Nick', 'John'],
    'Age': [20, 21, 19, 20, 21, 19],
    'Color': ['Red', 'Green', 'Blue', 'Red', 'Green', 'Blue']   
})
    
df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)  
else:
    st.write('Upload a CSV file')



    


#Display a simple text
st.write('This is a simple example of an EDA using Streamlit')
