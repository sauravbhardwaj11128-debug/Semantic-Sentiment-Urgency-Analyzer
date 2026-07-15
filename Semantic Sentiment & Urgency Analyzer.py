import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash")

st.title("Semantic Sentiment & Urgency Analyzer")

feedback = st.text_area("Enter Customer Feedback")

if st.button("Analyze"):

    prompt = f"""
Analyze the customer feedback.

Return ONLY JSON with:

- sentiment
- urgency
- complaint_or_praise

Feedback:
{feedback}
"""

    response = model.generate_content(prompt)

    st.write(response.text)
