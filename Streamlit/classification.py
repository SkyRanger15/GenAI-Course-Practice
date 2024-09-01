import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['species'] = data.target
    return df, data.target_names

df,target_names = load_data()
model = RandomForestClassifier()
X=df.iloc[:,:-1]
y=df['species']
model.fit(X,y)

st.sidebar.title("Iris Classifier")
sepallength = st.sidebar.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepalwidth = st.sidebar.slider("Sepal Width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petallength = st.sidebar.slider("Petal Length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petalwidth = st.sidebar.slider("Petal Width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

inputs = [[sepallength,sepalwidth,petallength,petalwidth]]

prediction = model.predict(inputs)
predicted_species = target_names[prediction][0]

st.write(f"The predicted species is {predicted_species}")
