import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import streamlit as st
from sklearn.linear_model import LinearRegression

def Package_prediction(cgpa, lr_model):
    cgpa = float(cgpa)
    prediction = lr_model.predict([[cgpa]])
    return prediction[0]

def main():
    st.title("Student Package Prediction")
    html_temp = """
        <div style="background-color: tomato; padding: 10px">
        <h2 style="color: white; text-align: center;">Student Package Prediction ML App</h2>
        </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Load the model from the pickle file
    with open("lr.pkl", "rb") as pickle_in:
        lr = pickle.load(pickle_in)
    
    cgpa = st.text_input("CGPA", "Type here")
    result = ""
    
    if st.button("Predict"):
        result = Package_prediction(cgpa, lr)
        st.success("The predicted package is {}".format(result))

if __name__ == '__main__':
    main()
