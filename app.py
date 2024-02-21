import pandas as pd
import numpy as np
import streamlit as st 
import pickle 

st.header("Predicttion Heart Deases" ,divider="rainbow")

df = pickle.load(open("Heart_deases_dataset.pkl" ,"rb"))
pipe = pickle.load(open("Pipeline.pkl" ,"rb"))


age = st.slider(
    'Select Your Age',
    0, 100)


sex = st.radio(
    "Select Your Gender",
    ["0", "1"],
    captions = ["Femal", "Male"],
    index=None)

chest_pain = st.radio(
    "Select Chest Pain Type",
    ["0", "1" ,"2" ,"3"],
    captions = ["asymptomatic", "non-anginal" ,"atypical_angina" ,"typical_angina"]
    ,index=None)

resting_bp = st.number_input("Enter Your Calculated BP")

cholestoral = st.number_input("Tell Your Cholestoral Leval : ")

fasting_blood_sugar = st.radio(
    "Tell About Fasting Blood Sugar Yes or No :",
    ["0", "1"],
    captions = ["Yes", "No"],
    index=None)

restecg = st.radio(
    "Tell Me Your Resting Electro Cardiographic Result",
    ["0" ,"1" ,"2"],
    captions=["Normal" ,"STT Abnormality" ,"LV Hypertrophy"],
    index=None)

max_hr = st.number_input("Enter Your Heart Beat Result ")

oldpeak = st.number_input("Enter Your ST depression induced(oldpeak)")

thal = st.radio(
    "Tell Me Your Thaesemia Test Result",
    ["0" ,"1" ,"2" ,"3"],
    captions=["Alpha thalassemia silent carrier" ,"Alpha thalassemia carrier" ,"Hemoglobin H disease" ,"Alpha thalassemia majo"],
    index=None
)

L = [age ,sex ,chest_pain ,resting_bp ,cholestoral ,fasting_blood_sugar ,restecg ,max_hr ,oldpeak ,thal]

try:
    if st.button('Predict'):

        pred = pipe.predict(pd.DataFrame(np.array(L).reshape(1,10) ,columns=['    age', 'sex', 'chest_pain_type', 'resting_bp', 'cholestoral' ,'fasting_blood_sugar', 'restecg', 'max_hr', 'oldpeak', 'thal']))

        st.subheader("" ,divider="rainbow")

        if(pred[0] == 1):
            st.subheader("Heart Deases Report Positive")
        else:
            st.subheader("Heart Deases Report Negative")
except:
    st.write("Somthing Went Wrong Pls Try Again !")