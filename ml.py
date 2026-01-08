import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title='Marks Predictor', layout='centered')

st.title('🧑🏻‍🎓 Student Marks Predictor')
st.write('Enter The Number of Hours Studied (1-10) And **Click Predict** To Get The Predicted Marks')

#load the model
def load_model(model):
    with open(model, 'rb') as f:
        slr = pickle.load(f)
    return slr

try:
    model = load_model('slr.pkl')
except Exception as e:
    st.error('Your pickle file not found ....')
    st.exception('Failed To Load The Model :',e)
    st.stop()

hours = st.number_input('Hours Studied',1.0,10.0,1.0)
predict_btn = st.button('Predict Score')

if predict_btn:
    prediction = model.predict([[hours]])
    st.success(f"Prediction Mark: {prediction[0]:.2f}")

