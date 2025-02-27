import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Title of the application

@st.cache
def load_data():
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df, data.target_names



def train_model(df):
    X = df.drop('target', axis=1)   
    y = df['target']
    clf = RandomForestClassifier()
    clf.fit(X, y)
    
    sepal_length=st.sidebar.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
    sepal_width=st.sidebar.slider("Sepal Width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))              
    petal_length=st.sidebar.slider("Petal Length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))          
    petal_width=st.sidebar.slider("Petal Width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))          
    
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = clf.predict(input_data)    
    prediction_proba = clf.predict_proba(input_data)                    
    st.write('Prediction')
    st.write(prediction)
    st.write('Prediction Probability')
    st.write(prediction_proba)
    #return clf

def main():
    st.title('Exploratory Data Analysis with Streamlit')
    st.write('This is a simple example of an EDA using Streamlit')
    
    df,target_names = load_data()
    st.write(df)
    
    train_model(df)
    #st.write(clf)
    
if __name__ == '__main__':
    main()
