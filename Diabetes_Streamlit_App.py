# Diabetes Detector
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import pickle

#!pip install -q streamlit

import streamlit as st
st.set_page_config(layout="wide")
st.title('Welcome to Diabetes Detection Data application')
st.write('This data application uses Random Forest Alogrithm to do prediction')
st.write('*******')
image = Image.open('Capture.JPG')

#image

# st.image(image,caption='ML',use_column_width=True)


def get_user_input():
  st.sidebar.header('Select Input Parameters')
  Pregnancies = st.sidebar.slider('Pregnancies',0,17,3)
  Glucose = st.sidebar.slider('Glucose',0,199,117)
  BloodPressure = st.sidebar.slider('BloodPressure',0,160,72)
  SkinThickness = st.sidebar.slider('SkinThickness',0,99,23)
  Insulin = st.sidebar.slider('Insulin',0.0,846.0,30.0)
  BMI = st.sidebar.slider('BMI',0.0,67.1,32.0)
  DiabetesPedigreeFunction = st.sidebar.slider('Diab. Pedigree Func',0.078,2.42,0.3725)
  Age = st.sidebar.slider('Age',20,100,40)

  user_data = {'Pregnancies': Pregnancies,
               'Glucose' : Glucose,
               'BloodPressure' : BloodPressure,
               'SkinThickness' : SkinThickness,
               'Insulin': Insulin,
               'BMI': BMI,
               'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
               'Age': Age
               }
  features = pd.DataFrame(user_data,index =[0])
  return features

user_input = get_user_input()

st.subheader('Patient entered medical data (as selected via slider on the left) : ')

st.write(user_input)

# Reads in saved classification model
load_clf = pickle.load(open('Diabetes_clf.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(user_input)


# st.subheader('Machine Learning Model Prediction: Patient is - ')
# st.write(prediction)

if prediction == 1:
  st.subheader('Machine Learning Model Prediction : Member is diabetic')
else:
 st.subheader('Machine Learning Model Prediction :  Member is non-diabetic')

# st.subheader('Machine Learning Model Confidence level(Test Accuracy Score) is :')
# st.write(str(accuracy_score(y_test,RandomForestClassifier.predict(X_test)) *100) +'%')
