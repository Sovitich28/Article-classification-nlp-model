# streamlit_app.py

import streamlit as st
import numpy as np
import joblib

# --- Load the trained Naive Bayes model ---
@st.cache_resource
def load_model():
    model = joblib.load('NB_model.pkl')
    return model

nb_model = load_model()

# --- Streamlit App UI ---
st.title(" News Article Category Predictor")
st.subheader("Using Multinomial Naive Bayes Model")

# Text input from the user
user_input = st.text_area("Enter a news article text here:", height=250)

if st.button("Predict Category"):
    if user_input.strip() == "":
        st.warning("Please enter some text to predict.")
    else:
        # Predict probabilities
        probabilities = nb_model.predict_proba([user_input])
        predicted_index = np.argmax(probabilities)
        predicted_category = nb_model.classes_[predicted_index]

        # Display results
        st.success(f"**Predicted Category:** {predicted_category}")
       
st.markdown("---")
