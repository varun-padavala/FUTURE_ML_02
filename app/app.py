import streamlit as st
from src.ticket_predictor import predict_ticket

st.title("Support Ticket Classification System")

text = st.text_area("Enter Support Ticket")

if st.button("Predict"):

    if text.strip():

        category, priority = predict_ticket(text)

        st.success(f"Category: {category}")
        st.warning(f"Priority: {priority}")

    else:
        st.error("Please enter a ticket")