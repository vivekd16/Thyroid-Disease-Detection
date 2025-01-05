import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model/thyroid_disease_model.pkl')

# Define the input form
st.title("Thyroid Disease Prediction")
st.write("Enter the patient details below:")

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0)
    query_hypothyroid = st.selectbox("Query Hypothyroid", options=["False", "True"])
    on_thyroxine = st.selectbox("On Thyroxine", options=["False", "True"])
    on_antithyroid_meds = st.selectbox("On Antithyroid Meds", options=["False", "True"])
    sick = st.selectbox("Sick", options=["False", "True"])
    pregnant = st.selectbox("Pregnant", options=["False", "True"])
    I131_treatment = st.selectbox("I131 Treatment", options=["False", "True"])
    TSH_measured = st.selectbox("TSH Measured", options=["False", "True"])
    T3_measured = st.selectbox("T3 Measured", options=["False", "True"])
    TT4_measured = st.selectbox("TT4 Measured", options=["False", "True"])
    T4U_measured = st.selectbox("T4U Measured", options=["False", "True"])
    FTI_measured = st.selectbox("FTI Measured", options=["False", "True"])
    TBG_measured = st.selectbox("TBG Measured", options=["False", "True"])
    thyroid_surgery = st.selectbox("Thyroid Surgery", options=["False", "True"])

with col2:
    sex = st.selectbox("Sex", options=["Female", "Male"])
    query_hyperthyroid = st.selectbox("Query Hyperthyroid", options=["False", "True"])
    query_on_thyroxine = st.selectbox("Query on Thyroxine", options=["False", "True"])
    lithium = st.selectbox("Lithium", options=["False", "True"])
    goitre = st.selectbox("Goitre", options=["False", "True"])
    tumor = st.selectbox("Tumor", options=["False", "True"])
    psych = st.selectbox("Psych", options=["False", "True"])
    TSH = st.number_input("TSH", min_value=0)
    T3 = st.number_input("T3", min_value=0)
    TT4 = st.number_input("TT4", min_value=0)
    T4U = st.number_input("T4U", min_value=0)
    FTI = st.number_input("FTI", min_value=0)
    TBG = st.number_input("TBG", min_value=0)

# Create a DataFrame for the input data
input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'on_thyroxine': [on_thyroxine],
    'query_on_thyroxine': [query_on_thyroxine],
    'on_antithyroid_meds': [on_antithyroid_meds],
    'sick': [sick],
    'pregnant': [pregnant],
    'thyroid_surgery': [thyroid_surgery],
    'I131_treatment': [I131_treatment],
    'query_hypothyroid': [query_hypothyroid],
    'query_hyperthyroid': [query_hyperthyroid],
    'lithium': [lithium],
    'goitre': [goitre],
    'tumor': [tumor],
    'psych': [psych],
    'TSH_measured': [TSH_measured],
    'TSH': [TSH],
    'T3_measured': [T3_measured],
    'T3': [T3],
    'TT4_measured': [TT4_measured],
    'TT4': [TT4],
    'T4U_measured': [T4U_measured],
    'T4U': [T4U],
    'FTI_measured': [FTI_measured],
    'FTI': [FTI],
    'TBG_measured': [TBG_measured],
    'TBG': [TBG]
})

# Convert categorical variables from 'f'/'t' to 0/1
input_data.replace({'f': 0, 't': 1, 'False': 0, 'True': 1, "Female": 0, "Male": 1}, inplace=True)

# Button to make prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        st.write("Prediction: No thyroid disease")
    elif prediction[0] == 1:
        st.write("Prediction: Hyperthyroid disease")
    elif prediction[0] == 2:
        st.write("Prediction: Hypothyroid disease")