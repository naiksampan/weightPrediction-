import streamlit as st
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
import numpy as np
st.header("Human Weight Prediction App")
st.text_input("Enter your Name: ", key="name")
data = pd.read_csv("https://raw.githubusercontent.com/naiksampan/weightPrediction-/main/heightWeight.csv")
#load label encoder
encoder = LabelEncoder()
encoder.classes_ = np.load('classes.npy',allow_pickle=True)

# load model
best_xgboost_model = xgb.XGBRegressor()
best_xgboost_model.load_model("best_model.json")

if st.checkbox('Show Training Dataframe'):
    data

st.subheader("Please select your Height!")
left_column, right_column = st.columns(2)
with left_column:
    inp_species = st.radio(
        'Gender of the Person:',
        np.unique(data['Gender']))


input_Length1 = st.slider('Height(cm)', 137.828, max(data["Height"]), 139.0)



if st.button('Make Prediction'):
    input_species = encoder.transform(np.expand_dims(inp_species, -1))
    inputs = np.expand_dims(
        [int(input_species), input_Length1], 0)
    prediction = best_xgboost_model.predict(inputs)
    print("final pred", np.squeeze(prediction, -1))
    st.write(f"Your weight is: {np.squeeze(prediction, -1):.2f} kgs")

    st.write(f"Thank you {st.session_state.name}! I hope you liked it.")
    st.write(f"If you want to see more advanced applications you can follow me on [GitHub](https://github.com/naiksampan)")
    
# logging.basicConfig(filename='example.log')
# logging.debug('This message should go to the log file')
