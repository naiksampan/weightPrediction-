import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
import numpy as np
st.header("Human Weight Prediction App")
st.text_input("Enter your Name: ", key="name")
data = pd.read_csv("https://raw.githubusercontent.com/naiksampan/weightPrediction-/main/weight-height.csv")
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
        'Gender of the Human:',
        np.unique(data['Gender']))


input_Length1 = st.slider('Height(cm)', 0.0, max(data["Height"]), 1.0)
#input_Length2 = st.slider('Diagonal length(cm)', 0.0, max(data["Length2"]), 1.0)
#input_Length3 = st.slider('Cross length(cm)', 0.0, max(data["Length3"]), 1.0)
#input_Height = st.slider('Height(cm)', 0.0, max(data["Height"]), 1.0)
#input_Width = st.slider('Diagonal width(cm)', 0.0, max(data["Width"]), 1.0)


if st.button('Make Prediction'):
    input_species = encoder.transform(np.expand_dims(inp_species, -1))
    inputs = np.expand_dims(
        [int(input_species), input_Length1], 0)
    prediction = best_xgboost_model.predict(inputs)
    print("final pred", np.squeeze(prediction, -1))
    st.write(f"Your weight is: {np.squeeze(prediction, -1):.2f}g")

    st.write(f"Thank you {st.session_state.name}! I hope you liked it.")
    st.write(f"If you want to see more advanced applications you can follow me on [GitHub](https://github.com/naiksampan)")
