import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Result Prediction App")

# Input fields
math = st.number_input("Enter Math Marks", 0, 100)
reading = st.number_input("Enter Reading Marks", 0, 100)
writing = st.number_input("Enter Writing Marks", 0, 100)

if st.button("Predict Result"):

    input_data = np.array([[math, reading, writing]])
    prediction = model.predict(input_data)

    total = math + reading + writing

    st.write("### Total Marks:", total)

    if total >= 250:
        st.success("Grade: A 🥇")
    elif total >= 200:
        st.success("Grade: B 🥈")
    elif total >= 150:
        st.success("Grade: C 🥉")
    else:
        st.error("Result: FAIL ❌")